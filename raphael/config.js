// initials

export default {

  container: 'paper',

  shared: {
      'stroke-width': 1,
      'fill-opacity': 0.2
  },

  signals: [ 'normal', 'warn', 'alarm' ],

  states: {

    initial: {
      
      shared: {
          stroke: 'gray',
          transform: 's1.0'
      },
      normal: {
          fill: 'lightgreen'
      },
      warn: {
          fill: 'lightyellow'
      },
      alarm: {
          fill: '#FFA650'
      }
    },

    hover: {
      shared: {
        stroke: 'lightgray',
        'fill-opacity': 0.25,
      },
      normal: {
          fill: 'lightgreen'
      },
      warn: {
          fill: 'lightyellow'
      },
      alarm: {
          fill: '#FFA650'
      }

    },

    active: {
      shared: {
        stroke: 'white',
        'fill-opacity': 0.7,
        'stroke-width': 2
      },
      normal: {
          fill: 'lightgreen'
      },
      warn: {
          fill: 'lightyellow'
      },
      alarm: {
          fill: '#FFA650'
      }
    },

    disabled: {
        shared: {
            'fill-opacity': 0.1,
            transform: 's1.0',
            stroke: 'gray'
        }
    }
  }
};