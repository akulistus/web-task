function sendData(button) {
    const Id = button.getAttribute('data-bs-Id');
    fetch('/create-appointment',{
        method:'POST',
        body: JSON.stringify({id: Id}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        location.reload();
    });
};