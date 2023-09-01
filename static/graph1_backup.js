import {} from "./chart.js";
import {} from "./d3.v6.js";
import {} from "./highcharts.js";
import {} from "./accessibility.js";
import {} from "./export-data.js";
import {} from "./exporting.js";



// New JSON object with int numbers in data converted to lists
const json3_new = json3.map((obj) => {
    return {
        ...obj,
        data: [obj.data]
    };
});

console.log(json3_new)



var chart2 = new Highcharts.chart({
    chart: {
      renderTo:'graph1',
      type: 'column',
      inverted: false,
    },
    title: {
      text: 'Most Classified'
    },
    xAxis: {
      categories: ['Sample 1']
    },
    yAxis: {
      title: {
        text: 'Reads Classified'
      }
    },
    series: json3_new });
    
    
console.log(json3_new)
