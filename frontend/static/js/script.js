async function loadData(){

let response = await fetch("/api/data")
let data = await response.json()

document.getElementById("object").innerText = data.object
document.getElementById("threat").innerText = data.threat

}

setInterval(loadData,2000)

loadData()


const ctx = document.getElementById('threatChart');

new Chart(ctx, {
type: 'line',
data: {
labels: ['1','2','3','4','5'],
datasets: [{
label: 'Threat Activity',
data: [1,3,2,5,4],
borderWidth: 2
}]
}
});