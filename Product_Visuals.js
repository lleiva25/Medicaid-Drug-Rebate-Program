// Fetch the JSON data and console log it
d3.json("/Users/leslieleiva/Documents/GitHub/Medicaid-Drug-Rebate-Program/Output/Product_Data_2023").then((data) => {
    // Populate the dropdown menu
    var select = d3.select("#selDataset");
    data.product_name.forEach((product_name) => {
        select.append("option").text(product_name).property("value", product_name);
    });

    // Add event listener for the dropdown menu change
    select.on("change", function () {
        var newSample = d3.select(this).property("value");
        optionChanged(newSample);
    });

        // Initialize the page with the first sample
        var firstMed = data.product_name[0];
        buildCharts(firstMed);
        buildMetadata(firstMed);
        // Initialize the page with the first sample for gauge chart
        buildGaugeChart(firstMed); 
    });


// Function to build the metadata panel
function buildMetadata(sample) {
    d3.json("/Users/leslieleiva/Documents/GitHub/Medicaid-Drug-Rebate-Program/Output/Product_Data_2023").then((data) => {
        var metadata = data.metadata;
        var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
        var result = resultArray[0];
        var PANEL = d3.select("#sample-metadata");

        // Clear any existing metadata
        PANEL.html("");

        // Add each key-value pair to the panel
        Object.entries(result).forEach(([key, value]) => {
            PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
        });
    });
}