# ✅ MOCK BLOCKCHAIN DATA (for testing)

transactions = [
    {
        "from": "0xabc123",
        "to": "0xdef456",
        "value": "5000000000000000000",
        "hash": "0xhash1"
    },
    {
        "from": "0xabc123",
        "to": "0xxyz789",
        "value": "9000000000000000000",
        "hash": "0xhash2"
    },
    {
        "from": "0xaaa111",
        "to": "0xbbb222",
        "value": "100000000000000000",
        "hash": "0xhash3"
    }
]

print("\n--- Sample Transactions ---\n")

for tx in transactions:
    print("From:", tx['from'])
    print("To:", tx['to'])
    print("Value:", tx['value'])
    print("Hash:", tx['hash'])
    print("-------------------------")
    

import sqlite3

# Connect to database
conn = sqlite3.connect("blockchain.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    hash TEXT,
    sender TEXT,
    receiver TEXT,
    value REAL
)
""")

# Insert data into table
for tx in transactions:
    cursor.execute("""
    INSERT INTO transactions (hash, sender, receiver, value)
    VALUES (?, ?, ?, ?)
    """, (tx['hash'], tx['from'], tx['to'], float(tx['value'])))

# Save and close
conn.commit()
conn.close()

print("\n✅ Data saved to database successfully!")

print("\n--- Suspicious Transactions Detection ---\n")

for tx in transactions:
    value = int(tx['value'])

    # Rule 1: Large transaction
    if value > 7000000000000000000:
        print("⚠ Suspicious Large Transaction Detected!")
        print("From:", tx['from'])
        print("To:", tx['to'])
        print("Value:", tx['value'])
        print("Hash:", tx['hash'])
        print("-------------------------")
        
        


print("\n--- Suspicious Wallet Activity ---\n")

wallet_count = {}

# Count transactions per sender
for tx in transactions:
    sender = tx['from']
    
    if sender in wallet_count:
        wallet_count[sender] += 1
    else:
        wallet_count[sender] = 1

# Detect suspicious wallets
for wallet, count in wallet_count.items():
    if count > 1:
        print("⚠ Suspicious Wallet Detected!")
        print("Wallet Address:", wallet)
        print("Number of Transactions:", count)
        print("-------------------------")