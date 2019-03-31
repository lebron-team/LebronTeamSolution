import Raphael from '@/raphael/raphael.min.js';
import { composeStyles } from '@/raphael/util.js';
import Region from '@/raphael/Region.js';
import EventEmitter from '@/raphael/EventEmitter.js';

export default class Intermap extends EventEmitter {

  constructor(config, regions) {
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
              this.emit('reset', id);
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