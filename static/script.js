async function searchTools() {
    const query = document.getElementById('search-bar').value;
    const response = await fetch(`/search?query=${query}`);
    const tools = await response.json();
    
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    tools.forEach(tool => {
        const toolElement = document.createElement('div');
        toolElement.innerHTML = `<h3>${tool.name}</h3><p>${tool.description}</p><p>Category: ${tool.category}</p>`;
        resultsDiv.appendChild(toolElement);
    });
}
