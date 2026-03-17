  inputs = document.getElementsByTagName("input");
  resultDiv = document.getElementById('result')
for (let i = 0; i < 3; i++) {
    j = inputs[i];
    j.addEventListener('change', function(){
      if (j.value == '')
        j.style.border = 'red solid 2px'
      else j.style.border = ''
    })
}
async function regist(e) {
if (document.getElementById('country').value == "" && document.getElementById('country') != 'de'){
   document.getElementById('country').style.border = 'solid 2px red'
  resultDiv.innerText = 'choose county'
  return false
  }
   for (let i = 0; i < 3; i++) {
    j = inputs[i];
    if (j.value == "") {
      j.style.border = "solid red 2px";
      return false;
    }
  }
  e.preventDefault();
  code = document.getElementById("code").innerText;
  req = {
    code: code,
    country: document.getElementById("country").value,
    state: document.getElementById("states").value.replace(' ' , '+'),
    first_name: document.getElementById("first_name").value,
    last_name: document.getElementById("last_name").value,
    email: document.getElementById('email').value,
    mobile_carrier: document.getElementById('mobile_carrier').value
  };
  try {
        const response = await fetch('/regist', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(req)
        });
        content_type = response.headers.get('content-type')
        

        if (response.ok && content_type.includes('application/json')) {
          const data = await response.json();
        //   if (!data.is_active && !data.country_found){
        //     resultDiv.innerText = 'البلد غير متاح الآن'
        //    resultDiv.style.color = data.is_active? 'green' : 'red';

            // return false
          // }
          if (!data.is_active){
            resultDiv.innerText = 'الكود غير موجود أو مستخدم بالفعل'
            resultDiv.style.color = data.is_active? 'green' : 'red';

            return false
          }
            else if(data.is_active){
            resultDiv.innerHTML  = 'redirecting'
            window.location.replace(data.redirect)
            // console.log(data.redirect)
            }
        resultDiv.style.color = data.is_active? 'green' : 'red';
        }
        else {
          resultDiv.textContent = data.error || 'Something went wrong.';
          resultDiv.style.color = 'orange';
        }
      } catch (error) {
        resultDiv.textContent = 'Error connecting to server.';
        resultDiv.style.color = 'orange';
      }
  
}
document.getElementById("regist").addEventListener("click", regist);
// 4LWg5bvQ

const countrySelect = document.getElementById("country");
const stateSelect = document.getElementById("states");

const statesByCountry = {
  usa: [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
  ],
  uk: [
    "England",
    "Scotland",
    "Wales",
    "Northern Ireland",
    "Greater London",
    "West Midlands",
    "Greater Manchester",
    "Merseyside",
    "West Yorkshire",
    "South Yorkshire",
    "Kent",
    "Surrey",
    "Essex",
    "Lancashire",
    "Devon",
    "Cornwall",
    "Norfolk",
    "Suffolk",
    "Cambridgeshire",
    "Oxfordshire",
    "Gloucestershire",
    "Hampshire",
    "Dorset",
    "Somerset",
    "Cheshire",
    "Derbyshire",
    "Nottinghamshire",
    "Leicestershire",
    "Staffordshire",
    "Warwickshire",
    "North Yorkshire",
    "East Yorkshire",
    "South Ayrshire",
    "Highland",
    "Dumfries and Galloway",
    "Tyne and Wear",
    "West Lothian",
    "Fife",
    "Aberdeenshire",
    "Perthshire and Kinross",
    "Moray",
    "Inverclyde",
  ],
};

countrySelect.addEventListener("change", function () {
  stateSelect.style.display = 'block'
  const selectedCountry = this.value;
  const states = statesByCountry[selectedCountry] || [];

  // Clear previous options
  stateSelect.innerHTML = '<option value="">Select State/Region</option>';

  // Populate new options
  states.forEach((state) => {
    const option = document.createElement("option");
    option.value = state;
    option.textContent = state;
    stateSelect.appendChild(option);
  });
});
