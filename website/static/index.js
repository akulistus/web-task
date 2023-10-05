function updateFormAction(button) {
    const doc_id = button.getAttribute('data-bs-docId')
    const pat_id = button.getAttribute('data-bs-patId')

    document.getElementById("myForm").setAttribute("action", `/edit-appointment/?doc_id=${doc_id}&pat_id=${pat_id}`)
}

function submitForm() {
    var form = document.getElementById("myForm");
    form.submit();
}

const exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', event => {

  const button = event.relatedTarget

  const recipient = button.getAttribute('data-bs-info')

  const modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalBodyInput.value = recipient
})
