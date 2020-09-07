// create charts using SDK (Mongodb Charts)
//create a new instance to create the first chart
const sdk = new ChartsEmbedSDK({
    baseUrl: 'https://charts.mongodb.com/charts-project-0-lbzdl'
});
        
const chart = sdk.createChart({
    chartId: '6b18b667-5d0c-4d0c-9f2b-ec0c20d2068f' ,
    height: "700px"          
});

//create a new instance to create the second chart
const sdk1 = new ChartsEmbedSDK({
    baseUrl: 'https://charts.mongodb.com/charts-project-0-lbzdl'
});

const piechart = sdk1.createChart({
    chartId: 'e670de67-f0cc-476b-ae50-f10ad455296e' , // Optional: ~REPLACE~ with the Chart ID from your Embed Chart dialog
    height: "700px",
    top:"800px"          
});

//render the charts
chart.render(document.getElementById('chart'));
piechart.render(document.getElementById('piechart'));