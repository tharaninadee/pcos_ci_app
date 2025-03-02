function drawPieChart(probability) {
    console.log("Drawing Pie Chart with Probability:", probability);  // Log probability to confirm

    let ctx = document.getElementById("pcosChart").getContext("2d");
    new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["PCOS Risk", "No Risk"],
            datasets: [{
                data: [probability, 100 - probability],
                backgroundColor: ["#ff6384", "#36a2eb"]
            }]
        }
    });
}
