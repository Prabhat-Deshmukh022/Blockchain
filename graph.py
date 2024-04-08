import matplotlib.pyplot as plt
import networkx as nx

# Sample transactions data
transactions = [
    {"sender_address": "15YxmJhVXNbdmWezS6hr1nsSr7eEVxRwR8", "receiver_address": "1LPaChxJc4dff3JCYyd4h1KWH87co6Dakt", "amount": 2.99992991},
    {"sender_address": "12hnzZXHghdqAoeeGXfbEDeKCiUhMoR4hj", "receiver_address": "17zwdnXbjJ6JWxfpv5VdirYDfMWnjFR3bU", "amount": 0.01002883},
    {"sender_address": "1AzxqWjjcjxphAfLmrFw19bSxAEHcmyxtH", "receiver_address": "15hjhNbufJw6vUFe4u9vh7XqNdsykMQZAM", "amount": 0.01600000},
    {"sender_address": "1sZ3yTZvoJrZJtErVFzsnhM3xSUieJgVC", "receiver_address": "14bzPbMmKvH3U9e3sTBfCDcKToVoD8vHqY", "amount": 0.70000000},
    {"sender_address": "14KoXQSMVMjYeeixf6kwEio3Bh4jumh9CN", "receiver_address": "1B2RXVgJBWjmsDHubKbfwoKCKccGwUEHiQ", "amount": 0.11406230},
    {"sender_address": "1NR2s54JQ8NZdqqRZAqRb1ffULCBR9Jorn", "receiver_address": "1NkuTbNk5HmWqXXceeddakUWmTUSKm58Yu", "amount": 2.70000000},
    {"sender_address": "1DAyvdyBDqeuUsv4CPBdX4pqf8SjerDYCw", "receiver_address": "1LX9def62XBbBS7bvyowz1qPb1MitHaZDV", "amount": 1.58700000},
    {"sender_address": "196WDb2bMDd1vP2Vugcac5ko1g66AeQ4kS", "receiver_address": "1KdN4SLLmT8jb79WjfGq9fsq19wYeX562b", "amount": 0.13048109},
    {"sender_address": "1Gr3WdmuEiScCJFYcJ6P9aiwF7U6VwrJdt", "receiver_address": "1LR3aJS2Qu4BSFL8xCwaaCS6pnNMbej8HE", "amount": 0.01028617},
    {"sender_address": "12gTidjaKvSShDLdMXNm4VCPZs4HJqjfEy", "receiver_address": "1NAj32Pju4jAortZ89adRjhmckT1XY7de7", "amount": 65.27576373},
    {"sender_address": "12gTidjaKvSShDLdMXNm4VCPZs4HJqjfEy", "receiver_address": "1LQsYyveKRNmtSh4TZhZbWo6jNGhrtarVu", "amount": 0.25600000},
    {"sender_address": "12gTidjaKvSShDLdMXNm4VCPZs4HJqjfEy", "receiver_address": "1LCe8o7VpcseGfJ8UCeNapqZhgobYkPES2", "amount": 0.25600000},
    {"sender_address": "12gTidjaKvSShDLdMXNm4VCPZs4HJqjfEy", "receiver_address": "1KCT5vtGwGFAo99KQ9jzeRcFezRiRNiAhx", "amount": 0.25600000},
    {"sender_address": "1PGYqCKenS4zqun5Hkr8zzgh8dk4KYEG9D", "receiver_address": "1NRWUSo89WDf731PVMAPWJgEqbW1fM1RaF", "amount":0.01600000 },
    {"sender_address": "1PGYqCKenS4zqun5Hkr8zzgh8dk4KYEG9D", "receiver_address": "1FLci2fjXP4Vis29zR1qStPSXc129AuKoH", "amount":0.01600000 },
    {"sender_address": "184Pcriz1nahYdHxB18JVtfG6KboLmNbPQ", "receiver_address": "1DbGdEebjDkivmAjR5X6Lx4S1cwgqcvsmJ", "amount":0.01600000 },
    {"sender_address": "184Pcriz1nahYdHxB18JVtfG6KboLmNbPQ", "receiver_address": "1EUmR1ifqgvEkcYbMeFdaQJqT92rjN9inB", "amount":0.01600000 },
    {"sender_address": "18fQFXYvFeGqRQPy9hZsm6DWSY3dMR11LN", "receiver_address": "1DbGdEebjDkivmAjR5X6Lx4S1cwgqcvsmJ", "amount":0.01600000 },
    {"sender_address": "19v3j1wEMduo1Qdm7UQxF8tzCMdgttoX8J", "receiver_address": "1QDGQyWk1fggAKqy6ZqADyKQNzSXoxjeYx", "amount":0.00100000 },
    {"sender_address": "19v3j1wEMduo1Qdm7UQxF8tzCMdgttoX8J", "receiver_address": "1PLMgXG4txRjUDyKTkXCcHyNqzmMKiAKbj", "amount":0.00100000 },
    {"sender_address": "19v3j1wEMduo1Qdm7UQxF8tzCMdgttoX8J", "receiver_address": "1PLMgXG4txRjUDyKTkXCcHyNqzmMKiAKbj", "amount":0.00100000 },
    {"sender_address": "19v3j1wEMduo1Qdm7UQxF8tzCMdgttoX8J", "receiver_address": "1L1et1huPstZsY9ys5tbwrmBACrq13Eb2u", "amount":0.00100000 },
    {"sender_address": "19v3j1wEMduo1Qdm7UQxF8tzCMdgttoX8J", "receiver_address": "1KV26MLH1tm2brttnpHSf4P65fXoUzUzpe", "amount":0.00100000 },
    {"sender_address": "1qPDvmjApyYjL7ZuGoXWFgpR3akLpbHkM", "receiver_address": "1GVAvzhqpbPbK3PMfVTZMFCCJHWKkyRuds", "amount":0.00100000 },
    {"sender_address": "1qPDvmjApyYjL7ZuGoXWFgpR3akLpbHkM", "receiver_address": "1KAWyDBgJAYSjzt2rCUcQnKGCJxjfPnWP", "amount":0.00100000 },
    {"sender_address": "1DcTca7AKyxPXywjz6kChAabphVkMcWhaC", "receiver_address": "1MenD3YVdXS5AsSHN5xCRDFM8ju7LErgVG", "amount":0.00100000 },
    {"sender_address": "bc1qs604c7jv6amk4cxqlnvuxv26hv3e48cds4m0ew", "receiver_address": "bc1qa24tsgchvuxsaccp8vrnkfd85hrcpafg20kmjw", "amount":0.00100000 },



]

# Create a directed graph
G = nx.DiGraph()

for transaction in transactions:
    sender = transaction["sender_address"]
    receiver = transaction["receiver_address"]
    G.add_edge(sender, receiver)

# Define a function to find nodes forming anonymity sets based on amount
def find_anonymity_sets(transactions):
    amount_sets = {}
    for transaction in transactions:
        amount = transaction["amount"]
        if amount not in amount_sets:
            amount_sets[amount] = set()
        amount_sets[amount].add(transaction["sender_address"])
    return amount_sets

# Find anonymity sets
anonymity_sets = find_anonymity_sets(transactions)

# Compute the positions of all nodes
pos = nx.spring_layout(G)

# Get the nodes that have positions
valid_nodes = [node for node in G.nodes if node in pos]

# Draw the graph without node labels
nx.draw(G, pos, with_labels=False, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)

# Color nodes belonging to each anonymity set
for amount, nodes in enumerate(anonymity_sets.values(), start=1):
    valid_nodes_in_set = [node for node in nodes if node in valid_nodes]
    nx.draw_networkx_nodes(G, pos, nodelist=valid_nodes_in_set, node_color=f"C{amount}", node_size=1000)
for node in valid_nodes_in_set:
        x, y = pos[node]
        plt.text(x, y, node, fontsize=9, ha='center', va='center')

plt.title("Cryptocurrency Transactions Graph with Anonymity Sets")
plt.legend()
plt.show()