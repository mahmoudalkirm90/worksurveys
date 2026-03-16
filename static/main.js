
    async function checkCode() {
      const code = document.getElementById('codeInput').value;
      const resultDiv = document.getElementById('result');

      if (!code) {
        resultDiv.textContent = 'Please enter a code.';
        return;
      }

      try {
        const response = await fetch('/check_code', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ code })
        });
        content_type = response.headers.get('content-type')
        

        if (response.ok && content_type.includes('application/json')) {
          const data = await response.json();
          resultDiv.innerText = data.is_active?true:'الكود غير موجود أو مستخدم بالفعل'
          resultDiv.style.color = data.exists ? 'green' : 'red';
        
        }
        else if (response.ok && content_type.includes('text/html')) {
                const html = await response.text();
          document.open();
          document.write(html);
          document.close();
      
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