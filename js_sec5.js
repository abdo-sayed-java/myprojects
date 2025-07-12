let students = [
    {id: 1, name: "Abdo", age: 25 },
    {id: 2, name: "Ahmed", age: 20 },
    {id: 3, name: "Ali", age: 21 }
];

function getUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({students});
        }, 1000);
    });
}

let container = document.getElementById('studentInfo');

async function showUserInfo() {
    try {
        let { students } = await getUser();
        container.innerHTML = '';
        for (let i = 0; i < students.length; i++) {
            container.innerHTML += `
                <p>User ID: ${students[i].id}</p>
                <p>Name: ${students[i].name}</p>
                <p>Age: ${students[i].age}</p>
                <hr>
            `;
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

    } catch (error) {
        console.error("Error Loading user data:", error);
        container.innerHTML = `<p style="color:red;">Failed to load user data.</p>`;
    }
}
loadBtn.addEventListener('click', function handler(e) {
    showUserInfo();
    loadBtn.removeEventListener('click', handler);
});

