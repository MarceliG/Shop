var updateBtns = document.getElementsByClassName('update-cart')
console.log('hello')
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var product_id = this.dataset.product
        var action = this.dataset.action
        console.log('product_id:', product_id, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymusUser') {
            console.log('Not logged in')
        } else {
            update_user_order(product_id, action)
        }
    })
}

function update_user_order(product_id, action) {
    console.log('User is logged in, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'product_id': product_id, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}

