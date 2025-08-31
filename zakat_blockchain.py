import time
import hashlib

class Block:
    def __init__(self, index, transactions, previous_hash, roll_number):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions  # List of transaction dicts
        self.previous_hash = previous_hash
        self.roll_number = roll_number
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Computes SHA-256 hash of the block's contents, using roll_number as a seed.
        """
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.transactions) +
            str(self.previous_hash) +
            str(self.roll_number)
        )
        # Incorporate roll_number as seed by appending/prepending
        seed_string = str(self.roll_number)
        hash_input = seed_string + block_string + seed_string
        return hashlib.sha256(hash_input.encode()).hexdigest()

class Blockchain:
    def mine_block(self, transactions, roll_number):
        """
        Explicitly mine a block with given transactions and roll_number as seed.
        """
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), transactions, last_block.hash, roll_number)
        self.chain.append(new_block)
        return new_block

    def validate_chain(self):
        """
        Explicitly validate the blockchain and print results.
        """
        valid = self.is_chain_valid()
        if valid:
            print("Blockchain is valid.")
        else:
            print("Blockchain is INVALID!")
        return valid
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Genesis block uses a fixed roll_number seed
        genesis_block = Block(0, [], "0", "GENESIS")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        last_block = self.get_last_block()
        # Use sender's roll_number for block hash
        block_roll_number = transactions[0]['sender_roll_number'] if transactions and 'sender_roll_number' in transactions[0] else "GENESIS"
        new_block = Block(len(self.chain), transactions, last_block.hash, block_roll_number)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.hash:
                print(f"Block {i} has invalid previous hash.")
                return False
            if current.hash != current.compute_hash():
                print(f"Block {i} has been tampered.")
                return False
        return True

# Single global blockchain instance
GLOBAL_BLOCKCHAIN = Blockchain()

class Node:
    def mine(self, transactions):
        """
        Mine a block with this node's roll number as seed.
        """
        return GLOBAL_BLOCKCHAIN.mine_block(transactions, self.roll_number)

    def validate_blockchain(self):
        """
        Validate the global blockchain.
        """
        return GLOBAL_BLOCKCHAIN.validate_chain()
    
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.balance = 200
        self.transaction_history = []

    def calculate_zakat(self):
        return round(self.balance * 0.025, 2)

    def pay_zakat(self, receiver):
        zakat_amount = self.calculate_zakat()
        self.balance -= zakat_amount
        receiver.balance += zakat_amount
        transaction = {
            'sender': self.name,
            'sender_roll_number': self.roll_number,
            'receiver': receiver.name,
            'receiver_roll_number': receiver.roll_number,
            'zakat_amount': zakat_amount,
            'remaining_balance': self.balance,
            'timestamp': time.time()
        }
        self.transaction_history.append(transaction)
        receiver.transaction_history.append(transaction)
        GLOBAL_BLOCKCHAIN.add_block([transaction])

    def print_transaction_history(self):
        print(f"Transaction history for {self.name}:")
        for tx in self.transaction_history:
            print(tx)

    def print_blockchain(self):
        print("Global Blockchain:")
        for block in GLOBAL_BLOCKCHAIN.chain:
            print({
                'index': block.index,
                'timestamp': block.timestamp,
                'transactions': block.transactions,
                'previous_hash': block.previous_hash,
                'hash': block.hash,
                'roll_number': block.roll_number
            })
