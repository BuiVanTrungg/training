let express = require('express');
let apiRouters = require("./routes");
let bodyParser = require('body-parser');
let mongoose = require('mongoose');

let app = express();
let port = process.env.PORT || 5000;

app.listen(port)
/// allow access-cross
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Methods", "*");
    next();
});
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
 }));
app.use(bodyParser.json());
app.use('/api',apiRouters)

mongoose.connect('mongodb://localhost:27017/mydatabase',{ useNewUrlParser: true });
var db = mongoose.connection;
console.log('RESTful API server started on: ' + port);

