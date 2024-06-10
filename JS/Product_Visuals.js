//console.log("Hello world");

//Refer to URL. Future Proof: Do not reference local files may cause eror
const url = 'https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Product_Data_2023.json';

// function populateDropdown(url) {
//     // Fetch the JSON data and handle the response
//     d3.json(url).then(function(data) {
//         // Log the entire dataset to the console
//         console.log('This is Data', data);

//         // Populate the dropdown menu
//         var select = d3.select("#selDataset");

//         // Access the product names from the JSON data
//         var productNames = data.product_name; // Assuming 'product_name' is the key in your JSON data

//         // Iterate through the product names and add them to the dropdown
//         productNames.forEach(function(product) {
//             select.append("option")
//                 .text(product)
//                 .property("value", product);
//         });
//     });
// }

// populateDropdown(url)

function init(){ 

    // fetch the json data and console log it
    d3.json(url).then(function(data){
        // Log the entire dataset to the console
        console.log('This is Data', data);

        // Use D3 to select the dropdown menu
        let dropdownMenu = d3.select("#selDataset");

        // getting all names from json
        let product = data.product_name;

        // getting dropdown 
        names.forEach(function(product){
            dropdownMenu.append("option").text(product).property("value");
        });
       
        // pass first subject and call the functions
        chartvalues(product[0]);
        metadata(product[0]);
    });
};

// function when the subject id changes
function optionChanged(passedvalue) {

    chartvalues(passedvalue);
    metadata(passedvalue);
};

init()

// // function to 
// function chartvalues(passedvalue){

//     // json data
//     d3.json(url).then(function(alldata){

//         // retrieve all samples data
//         let  = data.samples;

//         // filter for each option/subject selected
//         let id = samples.filter(take=>take.id == passedvalue);

//         // get data for all charts
//         let sample_values = id[0].sample_values; 
//         let otu_ids = id[0].otu_ids; 
//         let otu_labels = id[0].otu_labels; 

//         // call function
//         charts(sample_values, otu_ids, otu_labels);

//     });