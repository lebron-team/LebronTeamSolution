import EventEmitter from '@/raphael/EventEmitter.js';
const Raphael = require("./raphael");

function createPath(points) {

  const start = points[0];
  let path = `M${start.x} ${start.y} L`;
  for (let point of points) {
      path += ` ${point.x} ${point.y}`;
  }
  path += ` ${start.x} ${start.y}`

  return path;
}


const markerStyles = {
  initial: {
    fill: '45-#F9F9F9-#B8B8B8',
    opacity: 1,
    'stroke-opacity': 1,
    transform: 't 0 -25'
  },
  active: {
    opacity: 1,
    'stroke-opacity': 1
  },
  disabled: {
    opacity: 0,
    'stroke-opacity': 0,
    fill: 'none',
  }
};

export default class Region extends EventEmitter {

constructor(map, points, marker, data) {

    if (!(points instanceof Array) || points.length < 3) throw new Error('Неверный массив координат');
    super();
    this.id = data.id;

    this.map = map;
    this.status = 'initial';  // active, disabled
    this.signal = data.signal;

    this.init(points, marker);
}

updateStyle() {
  const styles = this.map.getStyle(this.status, this.signal);
  this.path.attr(styles);
  
  let markerStyle = Object.assign({}, markerStyles[this.status]);

  if (this.isActive) {

    markerStyle = Object.assign(markerStyle, { fill: styles.fill })
  }
  this.markerElements.p.attr(markerStyle);
  this.markerElements.c1.attr(markerStyle);
  this.markerElements.c2.attr(markerStyle);
  this.marker.toFront();
}

get isActive() {
  return (this.status == 'active');
}

setSignal(signal) {
  this.signal = signal;
  this.updateStyle();
}

setStatus(status) {
  this.status = status;
  this.updateStyle();
}



init(points, marker) {

  const _this = this;

  this.path = this.map.raphael.path(createPath(points));
  

  this.markerElements = {
    p: this.map.raphael.path(`M ${marker.x - 10} ${marker.y} L ${marker.x + 10} ${marker.y} ${marker.x} ${marker.y + 25} ${marker.x - 10} ${marker.y}`).toFront(),
    c1: this.map.raphael.circle(marker.x, marker.y, 10).toFront(),
    c2: this.map.raphael.circle(marker.x, marker.y, 5).toFront()
  }

  this.marker = this.map.raphael.set(
    this.markerElements.p, this.markerElements.c1, this.markerElements.c2
  );

  this.marker.attr({
    fill: '45-lightgray-#222'
  });

  this.path.hover(
    function() {
      if (!_this.isActive) {
        this.attr(_this.map.getStyle('hover', _this.signal)).toFront();
        // if (_this.status != 'disabled') {
        //   _this.marker.attr(MARKER_HOVER).toFront();
        // }
      }
    },
    function() {
      if (!_this.isActive) {
        const status = (_this.status == 'disabled') ? 'disabled' : 'initial';
        this.attr(_this.map.getStyle(status, _this.signal)).toBack();
        
        // if (_this.status != 'disabled') {
        //   _this.marker.attr(MARKER_NORMAL).toFront();
        // }
      }
    });

  this.path.click(function() {
    const event = (_this.isActive) ? 'reset' : 'activate';
    _this.emit(event, _this);
  });

  this.updateStyle();
}
}