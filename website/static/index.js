function updateAppointment(button) {
    const doc_id = button.getAttribute('data-bs-docId');
    const pat_id = button.getAttribute('data-bs-patId');

    document.getElementById("myForm").setAttribute('data-bs-docId', `${doc_id}`);
    document.getElementById("myForm").setAttribute('data-bs-patId', `${pat_id}`);
};

function deleteAppointment(button) {
  const doc_id = button.getAttribute('data-bs-docId');
  const pat_id = button.getAttribute('data-bs-patId');

  fetch('/delete-appointment',{
      method:'POST',
      body: JSON.stringify({did: doc_id, pid: pat_id}),
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

function submitForm() {
  const form = document.getElementById("myForm");
  const doc_id = form.getAttribute("data-bs-docId");
  const pat_id = form.getAttribute("data-bs-patId");

  const formData = new FormData(form);
  formData.append("doc_id", `${doc_id}`);
  formData.append("pat_id", `${pat_id}`);
  fetch('/edit-appointment',{
    method:'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
      console.log(data);
      location.reload();
  });
};

const exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', event => {

  const button = event.relatedTarget

  const recipient = button.getAttribute('data-bs-info')

  const modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalBodyInput.value = recipient
})
