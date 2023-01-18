const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();

// Connect to the database
let db = new sqlite3.Database('packets.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the packets database.');
});

// Set the view engine and views folder location
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Define route handlers
app.get('/', (req, res) => {
    res.send("Welcome to Packets Database");
});

app.get('/packets', (req, res) => {
    db.all('SELECT * FROM packets', [], (err, rows) => {
        if (err) {
            throw err;
        }
        res.render('packets', { packets: rows });
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server started on port 3000');
});
