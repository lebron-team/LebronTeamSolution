class EventEmitter {

  constructor() {
    this.handlers = {};
  }
  
  on(eventName, handler) {

      if (eventName in this.handlers) {
          this.handlers[eventName].push(handler);
      } else {
          this.handlers[eventName] = [ handler ];
      }
  };

  off(eventName, handler) {
      //..
  };

  emit(eventName, args) {
      if (eventName in this.handlers) {
          
          for (let handler of this.handlers[eventName]) {
              setTimeout(() => { handler.call(this, args); }, 0);
          }
      }
  }
}