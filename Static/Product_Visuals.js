//console.log("Hello world");

//Refer to URL. Future Proof: Do not reference local files may cause eror
let url = 'https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Product_Data_2023';
//var json = null;
//Shows url link not data
//console.log(url)

// Fetch the JSON data and console log it
d3.json(url).then((data) => {
           console.log(data)
    // Populate the dropdown menu
     var select = d3.select("#selDataset");
     data.columns.forEach((column) => {
         select.append("option").text(column).property("value", column);
     })
    })
    // // Add event listener for the dropdown menu change
    // select.on("change", function () {
    //     var newProduct = d3.select(this).property("value");
    //     optionChanged(newProduct);
    // });



//     // Initialize the page with the first sample
//     var firstProduct = data.product_name[0];
//     //buildCharts(firstProduct);
//     //buildMetadata(firstProduct);
//     // Initialize the page with the first sample for gauge chart
//     //buildGaugeChart(firstProduct);
// });

/////////////////////////////////////////////////
// function buildMetadata(sample) {
//     d3.json(url).then((data) => {
//         var metadata = data.metadata;
//         var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
//         var result = resultArray[0];
//         var PANEL = d3.select("#sample-metadata");

//         // Clear any existing metadata
//         PANEL.html("");

//         // Add each key-value pair to the panel
//         Object.entries(result).forEach(([key, value]) => {
//             PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
//         });
//     });
// }

/////////////////////////////////////////////////
/////////////////////////////////////////////////
/////////////////////////////////////////////////
/////////////////////////////////////////////////
/////////////////////////////////////////////////
/////////////////////////////////////////////////

// function BarChart() {
//     d3.json(url).then((data) => {
//         var trace1 = {
//             x: [],
//             y: [],
//             name: 'Medicaid Reimbursed',
//             orientation: 'h',
//             marker: {
//                 color: 'rgba(55,128,191,0.6)',
//                 width: 1
//             },
//             type: 'bar'
//         };

//         //Non-Medicaid portion of total Reimbursed
//         var trace2 = {
//             x: [],
//             y: [],
//             name: 'Non-Medicaid Reimbursed',
//             orientation: 'h',
//             type: 'bar',
//             marker: {
//                 color: 'rgba(255,153,51,0.6)',
//                 width: 1
//             }
//         };


//         var data = [trace1, trace2];

//         //Add data into the graphs
//         data.forEach(function (val) {
//             trace1.x.push(val["product_name"]);
//             trace1.y.push(val["Medicaid Amount Reimbursed"]);
//             trace2.x.push(val["product_name"]);
//             trace2.y.push(val["Non-medicaid Amount Reimbursed"]);
//         });


//         var layout = {
//             title: 'Colored Bar Chart',
//             barmode: 'stack'
//         };

//         Plotly.newPlot('sample-metadata', data, layout)}


/////////////////////////////////////////////////
// Function to handle changes in the dropdown selection
function optionChanged(newProduct) {
    console.log("New sample selected:", newProduct);
    // buildCharts(newProduct);
    buildMetadata(newProduct);
    // buildGaugeChart(newProduct); 
}