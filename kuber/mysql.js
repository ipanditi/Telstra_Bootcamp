const mysql = require('mysql2/promise');

async function runMySQL() {
    const connection = await mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'admin',
        database: 'test'
    });

    // Create a table if it doesn't exist
    await connection.execute(`CREATE TABLE IF NOT EXISTS example (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        value INT
    )`);

    // Insert a row into the table
    await connection.execute('INSERT INTO example (name, value) VALUES (?, ?)', ['example', 100]);

    // Query the table
    const [rows] = await connection.execute('SELECT * FROM example');
    console.log(rows);

    await connection.end();
}

runMySQL().catch(console.error);
