const csrftoken = getCookie('csrftoken');
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
async function makeRequest(url, method='GET', body) {
    let headers={
        'X-CSRFToken': csrftoken
    }
    let response = await fetch(url, {method, headers:headers, body:body});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        return response
}
}
async function onClick(event) {
    event.preventDefault()
    let url = event.target.dataset.url
    let num1 = document.getElementById('num1').value
    let num2 = document.getElementById('num2').value
    let data = {"A": num1, "B": num2}

    let answer = await makeRequest(url, "POST", JSON.stringify(data))
    let result = document.getElementById('result')
    result.style.fontSize = '25px'
    result.innerText = `Result: ${answer.result}`;
    result.style.color = 'green'
    if (answer.status ) {
         result.innerText = `Result: ${answer.statusText}`;
        result.style.color = 'red'
    }
}


async function getToken() {
    let url = "http://127.0.0.1:8000/api/v1/get-csrf-token/"
        await fetch(url);
}

window.addEventListener('load', getToken)
