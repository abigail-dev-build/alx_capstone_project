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

function deletePost(postId) {
  fetch("/delete-post", {
    method: 'POST',
    body: JSON.stringify({ postId: postId }),

  })
  .then((response) => {
    console.log(response)
    if(response.status === 200) {
      window.location.href = "/"
    }
  })

}

const contentParagraph = document.getElementById('content');
const maxCharacters = 250;

const content = contentParagraph.textContent;

if (content.length > maxCharacters) {
  const truncatedContent = content.slice(0, maxCharacters) + '...';
  contentParagraph.textContent = truncatedContent;

  // You can also add a tooltip to show the full content on hover
  // contentParagraph.content = content;
}
