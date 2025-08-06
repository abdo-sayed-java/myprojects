document.addEventListener('DOMContentLoaded', function() {
    function updateCartCount() {
        fetch('/cart/count/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('cart-count').textContent = data.count;
            });
    }

    updateCartCount();

    const searchForm = document.getElementById('book-search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const params = new URLSearchParams(formData);
            window.location.href = `${this.action}?${params.toString()}`;
        });
    }

    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', function() {
            const input = this.parentElement.querySelector('.quantity-input');
            let value = parseInt(input.value);

            if (this.classList.contains('minus') && value > 1) {
                input.value = value - 1;
            } else if (this.classList.contains('plus') && value < 20) {
                input.value = value + 1;
            }

            this.closest('form').submit();
        });
    });

    const profilePicInput = document.getElementById('id_profile_picture');
    if (profilePicInput) {
        profilePicInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    document.getElementById('profile-pic-preview').src = event.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }
});