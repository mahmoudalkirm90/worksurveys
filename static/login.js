
resultDiv = document.getElementById('result')

document.getElementById('login').addEventListener('click' , async function(){
  req = {
    username: document.getElementById('username').value,
    password: document.getElementById('password').value
}

    try {
        const response = await fetch('https://mahmoudalkirm.pythonanywhere.com/dashboard_admin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(req)
        });
        content_type = response.headers.get('content-type')
        

        if (response.ok && content_type.includes('application/json')) {
          const data = await response.json();
          data.correct?true:resultDiv.innerHTML = 'incorrect email or passWord'
          data.correct?true:resultDiv.style.color = 'red'
        }
        else if (response.ok && content_type.includes('text/html')) {
                const html = await response.text();
                document.body.innerHTML= html
      
              } 
        else {
          resultDiv.textContent = 'Something went wrong.';
          resultDiv.style.color = 'orange';
        }
      } catch (error) {
        resultDiv.innertext = 'Error connecting to server.';
        resultDiv.style.color = 'orange';
      }
  
}
)