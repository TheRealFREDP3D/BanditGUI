document.getElementById('username-dropdown').addEventListener('change', function() {
    const username = this.value;
    fetch(`/get_level_info?username=${username}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('level-title').innerText = data.level;
            document.getElementById('level-description').innerText = data.description;
            document.getElementById('level-objective').innerText = data.objective;
        })
        .catch(error => console.error('Error fetching level info:', error));
});