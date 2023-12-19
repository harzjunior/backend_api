// static/user.js
function addUser() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    if (username && password) {
        fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            getUsers();
            
	// Clear input fields
            usernameInput.value = '';
            passwordInput.value = '';
	})
        .catch(error => console.error('Error:', error));
    } else {
        alert('Username and password cannot be empty!');
    }
}

function getUsers() {
    fetch('/api/users')
        .then(response => response.json())
        .then(data => displayUsers(data))
        .catch(error => console.error('Error:', error));
}

function displayUsers(users) {
    const userList = document.getElementById('userList');
    userList.innerHTML = '<h2>User List</h2><ul>';

    users.forEach(user => {
        const listItem = `<li>${user.username} - ${user.password}</li>`;
        userList.innerHTML += listItem;
    });

    userList.innerHTML += '</ul>';
}

