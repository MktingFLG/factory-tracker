const loadBtn = document.getElementById("loadFactories");
const factoryList = document.getElementById("factoryList");

loadBtn.addEventListener("click", async () => {
    factoryList.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/api/factories/");
        const factories = await response.json();

        factories.forEach(factory => {
            const li = document.createElement("li");
            li.textContent = `${factory.name} — ${factory.location}`;
            factoryList.appendChild(li);
        });
    } catch (error) {
        console.error("Error loading factories:", error);
    }
});
