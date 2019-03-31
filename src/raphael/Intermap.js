// import Raphael from '@/raphael/raphael.min.js';
import Region from '@/raphael/Region.js';
import EventEmitter from '@/raphael/EventEmitter.js';

function composeStyles(config) {

    function _compose(state, signal) {
          
      const shared1 = config.shared;
      const shared2 = config.states[state].shared;
      const main = config.states[state][signal];
    
      const result = Object.assign({}, shared1, shared2, main)
      return result;
    }
  
    const styles = {};
    for (let state in config.states) {
      styles[state] = {}
      for (let signal of config.signals) {
        styles[state][signal] = _compose(state, signal);
      }
    }
    return styles;
  }

export default class Intermap extends EventEmitter {

  constructor(config, regions) {
      debugger;
      super();
      this.raphael = Raphael(config.container);
      this.styles = composeStyles(config);

      this._signals = config.signals;

      this.regions = regions.map(r => new Region(this, r.areaPoints, r.marker, r.data));
      this.regions.forEach(s => {
          s.on('activate', sender => {
              console.log('activate ' + sender.id);
              this.selectSegment(sender.id);
              this.emit('select', id);
          });
          s.on('reset', sender => {

              console.log('deactivate ' + sender.id);
              this.resetSelection();
              this.emit('reset', sender.id);
          });
      });
  }

  getStyle(state, signal) {
      const result = this.styles[state] [this._signals[signal]];
      return result;
  }

  selectSegment(id) {
      this.regions.forEach(s => {
          s.setStatus((s.id === id) ? 'active' : 'disabled');
      });
  }
  resetSelection() {
      this.regions.forEach(s => {
          s.setStatus('initial');
      });
  }
}