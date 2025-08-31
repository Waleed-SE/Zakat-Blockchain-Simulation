# Zakat-Blockchain-Simulation

# Zakat Blockchain Simulation

A simulation of a blockchain system for Zakat (Islamic charity) payments, featuring both a Python backend and a Streamlit web interface. Each student acts as a blockchain node, and Zakat (2.5%) is automatically calculated and distributed using secure blockchain blocks.

---

## Features

- **Blockchain Implementation**: Secure, tamper-evident chain of blocks using SHA-256 hashing.
- **Zakat Calculation**: Automatic deduction of 2.5% Zakat from each node's balance.
- **Node Management**: Add student nodes with name and roll number.
- **Transaction Processing**: Pay Zakat from one node to another, recorded as blockchain transactions.
- **Blockchain Validation**: Verify the integrity of the blockchain.
- **Web Interface**: Interactive Streamlit app for easy management and visualization.

---

## File Structure

- `zakat_blockchain.py`: Core blockchain logic, including Block, Blockchain, and Node classes.
- `app.py`: Streamlit web application for interacting with the blockchain.
- `README.md`: Project documentation.
- `Assignment1.zip`, `output.docx`: Additional resources (not required for running the app).
- `__pycache__/`, `.git/`, `.gitattributes`: System and version control files.

---

## How It Works

### Blockchain & Zakat Logic

- **Block**: Contains index, timestamp, transactions, previous hash, roll number, and its own hash.
- **Blockchain**: Manages the chain, mining, validation, and genesis block creation.
- **Node**: Represents a student, tracks balance and transaction history, can pay Zakat to another node.

#### Zakat Payment Flow

1. Node calculates 2.5% of its balance as Zakat.
2. Zakat is deducted from sender and added to receiver.
3. Transaction is recorded and added to the blockchain as a new block.

---

## Streamlit App Usage

### 1. Add Student Nodes

- Enter student name and roll number in the sidebar.
- Click "Add Node" to create a new blockchain node.

### 2. Pay Zakat

- Select sender and receiver nodes.
- Click "Pay Zakat" to process the transaction and record it on the blockchain.

### 3. View Transaction History & Blockchain

- Expand each node to see its transaction history.
- View the global blockchain with all blocks and transactions.

### 4. Validate Blockchain

- Click "Validate Blockchain" to check the integrity of the chain.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit

### Installation

1. Clone this repository.
2. Install Streamlit:
   ```bash
   pip install streamlit
   ```

### Running the App

```bash
streamlit run app.py
```

---

## Example

1. Add two or more student nodes.
2. Pay Zakat from one node to another.
3. View transaction history and blockchain blocks.
4. Validate the blockchain.

---

## Security & Integrity

- Each block is hashed with SHA-256, including roll number as a seed.
- Blockchain validation checks for tampering and correct hash linkage.

---

## License

This project is for educational purposes.
