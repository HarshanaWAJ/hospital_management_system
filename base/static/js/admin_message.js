document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default form submit behavior

            const messageId = this.getAttribute('data-id');  // Get the message ID from the data-id attribute
            console.log(`Message ID: ${messageId}`);  // Check the message ID

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
                    console.log(`CSRF Token: ${csrfToken}`);  // Check if CSRF is being passed correctly

                    // Forming the URL and logging it for debugging
                    const url = `/delete-message/${messageId}/`;
                    console.log(`Sending DELETE request to: ${url}`);

                    // Make an AJAX request to delete the message
                    fetch(url, {
                        method: 'POST',  // Ensure this is a POST request
                        headers: {
                            'Content-Type': 'application/json',  // Specify the content type as JSON
                            'X-CSRFToken': csrfToken,  // Include the CSRF token for protection
                            'X-Requested-With': 'XMLHttpRequest'  // This header indicates that the request is AJAX
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);  // Log the response from the server
                        if (data.message === "Success") {
                            // On success, remove the message row from the table
                            document.getElementById(`message-row-${messageId}`).remove();
                            Swal.fire('Deleted!', 'Your message has been deleted.', 'success');
                            window.location.href = "/admin-message/";
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
