// ---------- REGISTER ----------
const nameIp = document.querySelector("#nameIp");
const passIp = document.querySelector("#passIp");
const btnP1 = document.querySelector("#btnP1");
const btnP1L = document.querySelector("#btnP1L");

if (btnP1) {
    btnP1.addEventListener("click", () => {
        const name = nameIp.value.trim();
        const password = passIp.value.trim();

        if (name === "" || password === "") {
            alert("please try again");
        } else {
            const user = { name, password };

            let users = JSON.parse(localStorage.getItem("users")) || [];
            users.push(user);

            localStorage.setItem("users", JSON.stringify(users));
            alert("Registered!");

            // ไปหน้า login
            window.location.href = "l.html";
        }
    });
}

if (btnP1L) {
    btnP1L.addEventListener("click", () => {      
         // ไปหน้า login
        window.location.href = "l.html";
    }
)};

// ---------- LOGIN ----------
const loginName = document.querySelector("#loginName");
const loginPass = document.querySelector("#loginPass");
const btnLogin = document.querySelector("#btnLogin");

if (btnLogin) {
    btnLogin.addEventListener("click", () => {
        const name = loginName.value.trim();
        const password = loginPass.value.trim();

        let users = JSON.parse(localStorage.getItem("users")) || [];

        const found = users.find(u => u.name === name && u.password === password);

        if (!found) {
            alert("Wrong name or password");
        } else {
            alert("Login Success!");
            window.location.href = "final.html"; // ไปหน้าสุดท้าย
        }
    });
}
