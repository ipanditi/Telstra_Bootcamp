// Define a custom error class
class BalanceException extends Error {
    constructor(message) {
        super(message);
        this.name = "BalanceException";
    }
}

// Define the Account class
class Account {
    constructor(name, type, balance) {
        this.name = name;
        this.type = type;
        this.balance = balance;
    }

    withdrawAmount(wamt) {
        if (wamt > this.balance) {
            throw new BalanceException("Balance low");
        } else {
            this.balance -= wamt;
            console.log(`Withdrawn, your available balance is ${this.balance}`);
            updateBalanceDisplay();
        }
    }

    depositAmount(dep) {
        if (dep <= 0) {
            throw new BalanceException("Deposit low");
        } else {
            this.balance += dep;
            console.log(`Deposited, your available balance is ${this.balance}`);
            updateBalanceDisplay();
        }
    }

    checkBalance() {
        if (this.balance <= 0) {
            throw new BalanceException("0 balance");
        } else {
            console.log(`Your balance is ${this.balance}`);
            updateBalanceDisplay();
        }
    }
}

// Initialize the account
const account = new Account("Vivek", "Savings", 2300);

// Update balance display
function updateBalanceDisplay() {
    document.getElementById('balanceAmount').textContent = `$${account.balance.toFixed(2)}`;
}

// Deposit function
function deposit() {
    const depositAmount = parseFloat(document.getElementById('depositAmount').value);
    try {
        account.depositAmount(depositAmount);
        showSuccess(`Deposited $${depositAmount.toFixed(2)}`);
    } catch (e) {
        if (e instanceof BalanceException) {
            showError(e.message);
        } else {
            console.error(`Unexpected error: ${e.message}`);
        }
    }
}

// Withdraw function
function withdraw() {
    const withdrawAmount = parseFloat(document.getElementById('withdrawAmount').value);
    try {
        account.withdrawAmount(withdrawAmount);
        showSuccess(`Withdrew $${withdrawAmount.toFixed(2)}`);
    } catch (e) {
        if (e instanceof BalanceException) {
            showError(e.message);
        } else {
            console.error(`Unexpected error: ${e.message}`);
        }
    }
}

// Show error message
function showError(message) {
    document.getElementById('message').innerHTML = `<p class="error">${message}</p>`;
}

// Show success message
function showSuccess(message) {
    document.getElementById('message').innerHTML = `<p class="success">${message}</p>`;
}

// Initialize and update chart with Chart.js
const ctx = document.getElementById('balanceChart').getContext('2d');
const balanceChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Deposit', 'Withdrawal'],
        datasets: [{
            label: 'Amount ($)',
            data: [0, 0],
            backgroundColor: ['#4caf50', '#f44336']
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function updateChart(depositAmount, withdrawAmount) {
    balanceChart.data.datasets[0].data[0] = depositAmount;
    balanceChart.data.datasets[0].data[1] = withdrawAmount;
    balanceChart.update();
}
