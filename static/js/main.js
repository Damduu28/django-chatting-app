const inputField = document.querySelector(".search--form input"),
        seachBtn = document.querySelector(".search--form button"),
        tabContent = Array.from(document.querySelectorAll(".content")),
        tablinks = Array.from(document.querySelectorAll(".tabs a")),
        pageTitle = document.querySelector(".page-title"),
        message = document.querySelector(".msg"),
        chats = document.querySelectorAll(".chat__username"),
        eyeIcons = document.querySelectorAll(".field-group i#eye-icon");

        

if (seachBtn != null) {
    seachBtn.addEventListener('click', () => {
        inputField.classList.toggle("active")
        seachBtn.classList.toggle("active")
        inputField.focus()
    })
}

if (inputField != null) {
    inputField.addEventListener('keyup', e => {
        let inputValue = e.target.value
        inputValue = inputValue.toLowerCase()
        for (let i = 0; i < chats.length; i++) {
            let parentChat = chats[i].parentNode.parentNode
            let chatUser = chats[i].innerText || chats[i].textContent
            chatUser = chatUser.toLowerCase()
    
            if (chatUser.includes(inputValue)) {
                parentChat.style.display = ""
            } else {
                parentChat.style.display = "none"
            }
        }
    })
}

document.addEventListener('click', e => {
    let isButton = e.target.matches("[data-dropdown-btn]")

    if (!isButton && e.target.closest("[data-dropdown]") != null) return
    

    let currenDropdown
    if (isButton) {
        currenDropdown = e.target.closest("[data-dropdown]")
        currenDropdown.classList.add("active")
    }

    document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
        if (dropdown == currenDropdown) return

        dropdown.classList.remove("active")
    })
})

tablinks.forEach((tab, idx) => {
    tab.addEventListener('click', () => { 
        tablinks.forEach(tb => {
            tb.classList.remove("active")
        })
        tabContent.forEach(content => {
            content.classList.remove("active")

            if (content.classList.contains("active")) {
                pageTitle.innerHTML = content.dataset.title
            }
        })
        tabContent[idx].classList.add("active")
        tablinks[idx].classList.add("active")

        tabContent.forEach(content => {
            if (content.classList.contains("active")) {
                pageTitle.innerText = content.dataset.title
            }
        })
    })
})

eyeIcons.forEach(icon => {
    icon.addEventListener('click', e => {
        let pwdField = e.target.previousElementSibling
        if (pwdField.type == "password") {
            pwdField.type = "text"
            e.target.classList.add("active")
        }else{
            pwdField.type = "password"
            e.target.classList.remove("active")
        }
    })
});


setTimeout(() => {
    if (message != null) {
        message.style.display = "none"
    }
}, 4000);
