document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('expense-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/add', {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        });
    });
});
