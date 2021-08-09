// Copyright (c) 2021 Jonathan Vice

function displayModal(id) {
    const modal = document.getElementById(id);
    const close = document.getElementById(id + "-close");

    modal.style.display = "block";

    close.onclick = () => {
        modal.style.display = "none";
    };

    window.onclick = (ev) => {
        if (ev.target == modal) {
            modal.style.display = "none";
        }
    };
}