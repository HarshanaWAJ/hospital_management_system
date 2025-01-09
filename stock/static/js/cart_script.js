// Function to display the cart in the popup
function updateCartView() {
    var cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    var cartList = document.getElementById('cartItems');
    
    // Clear the cart display before updating
    cartList.innerHTML = '';

    // Display each cart item
    cartItems.forEach(function(item) {
        var listItem = document.createElement('li');
        listItem.textContent = `${item.name} (x${item.quantity}) - $${item.totalPrice.toFixed(2)}`;

        // Add "Remove" icon button (using Bootstrap icon for trash)
        var removeButton = document.createElement('button');
        removeButton.classList.add('btn', 'btn-danger', 'btn-sm', 'ms-2');
        removeButton.innerHTML = '<i class="bi bi-trash"></i>';  // Bootstrap trash icon
        removeButton.onclick = function() {
            removeFromCart(item.id);  // Remove item when clicked
        };
        listItem.appendChild(removeButton);

        // Add "Edit Quantity" icon button (using Bootstrap icon for pencil)
        var editButton = document.createElement('button');
        editButton.classList.add('btn', 'btn-info', 'btn-sm', 'ms-2');
        editButton.innerHTML = '<i class="bi bi-pencil"></i>';  // Bootstrap pencil icon
        editButton.onclick = function() {
            editQuantity(item.id);  // Open edit dialog for quantity
        };
        listItem.appendChild(editButton);

        cartList.appendChild(listItem);
    });
}

// Function to open the cart popup
document.getElementById('openCart').addEventListener('click', function() {
    document.getElementById('cartPopup').style.display = 'block';
    updateCartView(); // Update the cart content when the popup is opened
});

// Function to close the cart popup
document.getElementById('closeCart').addEventListener('click', function() {
    document.getElementById('cartPopup').style.display = 'none';
});

// Function to add items to the cart
function addToCart(stockId) {
    // Use SweetAlert2 to ask for the quantity
    Swal.fire({
        title: 'Enter Quantity',
        input: 'number',
        inputPlaceholder: 'Quantity',
        inputAttributes: {
            min: 1,
            max: 1000,
            step: 1
        },
        showCancelButton: true,
        confirmButtonText: 'Add to Cart',
        cancelButtonText: 'Cancel',
        preConfirm: (quantity) => {
            if (quantity && quantity > 0) {
                // Get the stock details dynamically
                var stockName = document.querySelector(`#stock-${stockId} .stock-name`).textContent;
                var stockPrice = parseFloat(document.querySelector(`#stock-${stockId} .stock-price`).textContent.replace('$', ''));

                // Calculate the total price for this item
                var totalPrice = stockPrice * quantity;

                // Prepare cart item
                var cartItem = {
                    id: stockId,
                    name: stockName,
                    quantity: quantity,
                    totalPrice: totalPrice
                };

                // Retrieve cart from localStorage or initialize an empty array
                var cart = JSON.parse(localStorage.getItem('cart')) || [];
                
                // Check if item is already in the cart
                var existingItem = cart.find(item => item.id === stockId);
                if (existingItem) {
                    // Update the quantity and total price
                    existingItem.quantity += quantity;
                    existingItem.totalPrice = existingItem.quantity * stockPrice;
                } else {
                    // Add new item to the cart
                    cart.push(cartItem);
                }

                // Save updated cart to localStorage
                localStorage.setItem('cart', JSON.stringify(cart));

                // Update the cart view
                updateCartView();
            } else {
                Swal.showValidationMessage('Please enter a valid quantity');
            }
        }
    });
}

// Function to remove an item from the cart
function removeFromCart(stockId) {
    // Retrieve cart from localStorage
    var cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Filter out the item to remove
    cart = cart.filter(item => item.id !== stockId);

    // Save the updated cart
    localStorage.setItem('cart', JSON.stringify(cart));

    // Update the cart view
    updateCartView();
}

// Function to edit the quantity of an item in the cart
// Function to edit the quantity of an item in the cart
function editQuantity(stockId) {
    // Retrieve cart from localStorage
    var cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Find the item to edit
    var item = cart.find(item => item.id === stockId);

    if (item) {
        // Retrieve the stock's unit price (same as when adding to the cart)
        var stockPrice = parseFloat(document.querySelector(`#stock-${stockId} .stock-price`).textContent.replace('$', ''));

        // Use SweetAlert2 to ask for the new quantity
        Swal.fire({
            title: 'Enter New Quantity',
            input: 'number',
            inputValue: item.quantity,
            inputAttributes: {
                min: 1,
                max: 1000,
                step: 1
            },
            showCancelButton: true,
            confirmButtonText: 'Update Quantity',
            cancelButtonText: 'Cancel',
            preConfirm: (newQuantity) => {
                if (newQuantity && newQuantity > 0) {
                    // Update the item quantity and recalculate total price
                    item.quantity = newQuantity;
                    item.totalPrice = item.quantity * stockPrice;  // Recalculate total price

                    // Save updated cart to localStorage
                    localStorage.setItem('cart', JSON.stringify(cart));

                    // Update the cart view
                    updateCartView();
                } else {
                    Swal.showValidationMessage('Please enter a valid quantity');
                }
            }
        });
    }
}

