  function redirectToPost(postUrl) {
    window.location.href = postUrl
  }

function closeErrorAlert() {
    let element = document.getElementById('alert-error');
    element.style.display = 'none';
}

function closeSuccessAlert() {
    let element = document.getElementById('alert-success');
    element.style.display = 'none';
}