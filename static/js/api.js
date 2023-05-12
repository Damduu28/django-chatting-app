const add_btn = document.querySelectorAll('.add-fiend')
const update_btn = document.querySelectorAll('.update-fiend')

for (let i = 0; i < add_btn.length; i++) {
    add_btn[i].addEventListener('click', e => {
        let userId = e.target.dataset.user
        let action = e.target.dataset.action
        
        if (action === 'add') {
            let cancel__btn = e.target.previousElementSibling
            e.target.style.display = "none"
            cancel__btn.style.display = "block"
            addFriendResquest(userId, action)
        }
        
        
        if (action === 'cancel') {
            let add__btn = e.target.nextElementSibling
            add__btn.style.display = "block"
            e.target.style.display = "none"
            addFriendResquest(userId, action)
        }
        
        if (action === 'confirm') {
            addFriendResquest(userId, action)
        }

    });
}

function addFriendResquest(userId, action) {
    console.log('UserId:', userId, "Action:", action)
    
    let url = "/add-friend/"
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({'userId': userId, "action": action})
    })
        .then(response => response.json())
        .then(data => {
        console.log(data)
        location.reload()
    })
}


for (let i = 0; i < update_btn.length; i++) {
    update_btn[i].addEventListener('click', e => {
        let requestId = e.target.dataset.request
        let action = e.target.dataset.action
        
        if (action === 'confirm') {
            acceptFriendResquest(requestId, action)
        }

    });
}

function acceptFriendResquest(requestId, action) {
    console.log('RequestId:', requestId, "Action:", action)
    
    let url = "/accept-friend/"
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({'requestId': requestId, "action": action})
    })
        .then(response => response.json())
        .then(data => {
        console.log(data)
        location.reload()
    })
}