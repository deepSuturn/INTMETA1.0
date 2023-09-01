import {} from "./chart.js";
import {} from "./d3.v6.js"
import {} from "./highcharts.js"
import {} from "./accessibility.js";
import {} from "./export-data.js";
import {} from "./exporting.js";

// New JSON object with int numbers in data converted to lists
const json3_new = json3_2.map((obj) => {
    return {
        ...obj,
        data: [obj.data]
    };
});

function createChart(chartOptions) {
 return new Highcharts.Chart(chartOptions);
}

function resetOptions() {
	Highcharts.setOptions(initialOptions)
}



function colorScheme1() {
	const theme = theme1
	chart3.destroy()
	resetOptions();
	Highcharts.setOptions(theme);
	chart3 = createChart(chartOptions);
}
function colorScheme2() {
	const theme = theme2
	chart3.destroy()
	resetOptions();
	Highcharts.setOptions(theme);
	chart3 = createChart(chartOptions);
}
function colorScheme3() {
	const theme = theme3
	chart3.destroy()
	resetOptions();
	Highcharts.setOptions(theme);
	chart3 = createChart(chartOptions);
}
function colorScheme4() {
	const theme = theme4
	chart3.destroy()
	resetOptions();
	Highcharts.setOptions(theme);
	chart3 = createChart(chartOptions);
}
function colorScheme5() {
	const theme = theme5
	chart3.destroy()
	resetOptions();
	Highcharts.setOptions(theme);
	chart3 = createChart(chartOptions);
}



const chartOptions = {
      chart: {
      renderTo:'graph3',
      type: 'bar',
      inverted: false,
    },
    
plotOptions: {
    series: {
        borderRadius: 5
    }
    
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
    series: json3_new }




const theme1 = {
  colors: ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef", "#b33dc6", "#5f126b"],
};
const theme2 = {
  colors: ["#e60049", "#0bb4ff", "#50e991", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4", "#b3d4ff", "#00bfa0", "#00473c"],
};
const theme3 = {
  colors: ["#b30000", "#7c1158", "#4421af", "#1a53ff", "#0d88e6", "#00b7c7", "#5ad45a", "#8be04e", "#ebdc78", "#ada255"],
};

const theme4 = {
  colors: ["#ffb400", "#d2980d", "#a57c1b", "#786028", "#363445", "#48446e", "#5e569b", "#776bcd", "#9080ff", "#434fcc"],
};
const theme5 = {
  colors: ['#00152e', '#000f00', '#3d7e17', '#6e9d01', '#bb2c21', '#a50006', '#006c52', '#205cbe', '#5a96f4', '#2b789c'],
};



const initialOptions = JSON.parse(JSON.stringify(Highcharts.getOptions()));
Highcharts.setOptions(theme1);
let chart3 = createChart(chartOptions);


document.getElementById('color-scheme-1').addEventListener('click', () => {
	colorScheme1();
})
document.getElementById('color-scheme-2').addEventListener('click', () => {
	colorScheme2();
})
document.getElementById('color-scheme-3').addEventListener('click', () => {
	colorScheme3();
})
document.getElementById('color-scheme-4').addEventListener('click', () => {
	colorScheme4();
})
document.getElementById('color-scheme-5').addEventListener('click', () => {
	colorScheme5();
})
