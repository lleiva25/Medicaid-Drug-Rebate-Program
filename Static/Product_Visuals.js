console.log("Hello world");

//Refer to URL. Future Proof: Do not reference local files may cause eror
let url = 'https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Output/Product_Data_2023';

fetch(url)
.then(res => res.json())
.then(out =>
  console.log('Checkout this JSON!', out))
.catch(err => { throw err });