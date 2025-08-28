let test = document.getElementById("btn-nav1");

window.addEventListener('scroll', function () {
    const scrollY = window.scrollY;
    const triggerPoint = 150; // px scrolled from top

    if (scrollY > triggerPoint) {
        const desc2 = document.getElementById("desc2");
        desc2.classList.add("visible");

        // Optional: remove listener if only needed once
        window.removeEventListener('scroll', arguments.callee);
    }
});