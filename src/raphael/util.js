export default {
  composeStyles = function(config) {

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
  },
  
  createPath = function(points) {
  
    const start = points[0];
    let path = `M${start.x} ${start.y} L`;
    for (let point of points) {
        path += ` ${point.x} ${point.y}`;
    }
    path += ` ${start.x} ${start.y}`
  
    return path;
  }
}

