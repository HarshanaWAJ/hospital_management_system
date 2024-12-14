document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default form submit behavior

            const messageId = this.getAttribute('data-id');  // Get the message ID from the data-id attribute

            // Trigger SweetAlert2 confirmation
            Swal.fire({
                title: 'Are you sure?',
                text: "This action cannot be undone!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Yes, delete it!',
                cancelButtonText: 'No, cancel!',
            }).then((result) => {
                if (result.isConfirmed) {
                    // Get the CSRF token from the page's cookie or DOM
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    // Forming the URL and sending a POST request to the backend
                    const url = `/delete-message/${messageId}/`;

                    // Make an AJAX request to delete the message
                    fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',  // Specify the content type as JSON
                            'X-CSRFToken': csrfToken,  // Include the CSRF token for protection
                            'X-Requested-With': 'XMLHttpRequest'  // Indicate that this is an AJAX request
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.message === "Success") {
                            // On success, remove the message row from the table
                            document.getElementById(`message-row-${messageId}`).remove();
                            Swal.fire('Deleted!', 'Your message has been deleted.', 'success');
                            window.location.href = "/admin-message/";  // Redirect to refresh the table
                        } else {
                            Swal.fire('Error!', 'There was an issue deleting the message.', 'error');
                        }
                    })
                    .catch(error => {
                        Swal.fire('Error!', 'There was an issue with the request.', 'error');
                    });
                }
            });
        });
    });
});

