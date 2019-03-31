import config from '@/raphael/config.js';
import Intermap from '@/raphael/Intermap.js';

const A = { x: 20, y: 40 };
const B = { x: 80, y: 20 };
const C = { x: 130, y: 100 };
const D = { x: 40, y: 120 };
const E = { x: 90, y: 180 };
const F = { x: 220, y: 50 };
const G = { x: 200, y: 110 };
const H = { x: 280, y: 140 };

const M0 = { x: 70, y: 70 };
const M1 = { x: 170, y: 70 };
const M2 = { x: 230, y: 100 };
const M3 = { x: 170, y: 140 };
const M4 = { x: 90, y: 140 }; 

export default function(){

  return new Intermap(config, [
    {
      data: {
        id: 0,
        signal: 0
      },
      marker: M0,
      areaPoints: [ A, B, C, D ]
    },
    {
      data: {
        id: 1,
        signal: 1
      },
      marker: M1,
      areaPoints: [ B, F, G, C ]
    },
    {
      data: {
        id: 2,
        signal: 2
      },
      marker: M2,
      areaPoints: [ G, F, H ]
    },
    {
        
      data: {
        id: 3,
        signal: 0
      },
      marker: M3,
      areaPoints: [ E, C, G, H ]
    },
    {
      id: 4,
      data: {
        id: 4,
        signal: 0
      },
      marker: M4,
      areaPoints: [ D, C, E ]
    }
]);
}