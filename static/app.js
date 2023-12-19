// static/script.js
function addUser() {
    const form = document.getElementById('addUserForm');
    const formData = new FormData(form);

    fetch('/api/add_user', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        form.reset();
    })
    .catch(error => console.error('Error:', error));
}

function getUsers() {
    fetch('/api/users')
    .then(response => response.json())
    .then(data => {
        const userList = document.getElementById('userList');
        userList.innerHTML = '<h2>Users</h2>';

        if (data.length > 0) {
            const ul = document.createElement('ul');
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `${user.username} - ${user.password}`;
                ul.appendChild(li);
            });
            userList.appendChild(ul);
        } else {
            userList.innerHTML += '<p>No users found.</p>';
        }
    })
    .catch(error => console.error('Error:', error));
}

