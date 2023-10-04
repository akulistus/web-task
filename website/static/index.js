function updateFormAction(button) {
    // Get the URL from the "data-bs-info" attribute of the clicked button
    const doc_id = button.getAttribute('data-bs-docId')
    const pat_id = button.getAttribute('data-bs-patId')
    // Set the new URL as the form's action
    document.getElementById("myForm").setAttribute("action", `/edit-appointment/${doc_id},${pat_id}`)
}

function submitForm() {
    var form = document.getElementById("myForm");
    form.submit(); // This will submit a POST request to the form's action path
}

const exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', event => {
  // Button that triggered the modal
  const button = event.relatedTarget
  // Extract info from data-bs-* attributes
  const recipient = button.getAttribute('data-bs-info')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalBodyInput.value = recipient
})
