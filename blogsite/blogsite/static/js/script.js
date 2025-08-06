document.querySelectorAll('.post').forEach(post => {
    post.addEventListener('click', () => {
        alert("You Clicked The Post")
    })
})