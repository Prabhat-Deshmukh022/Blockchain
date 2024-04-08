const express = require('express');
const bodyParser = require('body-parser');
const Blockchain = require('../blockchain');
const P2pServer = require('./p2p-server');
const Wallet = require('../wallet');
const TransactionPool = require('../wallet/transaction-pool');
const Miner = require('./miner');

const HTTP_PORT = process.env.HTTP_PORT || 3001;

const app = express();
const bc = new Blockchain();
const wallet = new Wallet();
const tp = new TransactionPool();
const p2pServer = new P2pServer(bc, tp);
const miner = new Miner(bc, tp, wallet, p2pServer);
//const env = Object.assign({}, process.env);

// env.HTTP_PORT = '3002';
// env.P2P_PORT = '5002';
// env.PEERS = 'ws://localhost:5001';

// console.log('Environment variables set successfully.');

// // Print the modified environment variables for verification
// console.log(env);

app.use(bodyParser.json());
const path = require('path'); // Import the path module
//app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.status(200).sendFile(path.join(__dirname, 'Final_Website.html'));
});

app.get('/home1', (req,res) => {
  res.status(200).sendFile(path.join(__dirname, "home1.html"))
})

app.get('/about', (req,res) => {
  res.status(200).sendFile(path.join(__dirname, "about1.html"))
})

app.get('/blocks', (req, res) => {
  res.json(bc.chain);
});

app.get('/contact', (req, res) => {
  res.status(200).sendFile(path.join(__dirname, "contact.html"))
})

app.post('/mine', (req, res) => {
   const block = bc.addBlock(req.body.data);
   console.log(`New block added: ${block.toString()}`);

   p2pServer.syncChains();

   res.redirect('/blocks');
});

// app.get('/transactions', (req, res) => {
//   res.sendFile(path.join(__dirname, 'output.html'));
// });

app.get('/transactions', (req, res) => {
  res.json(tp.transactions);
})

app.post('/transact', (req, res) => {
   const { recipient, amount } = req.body;
   const transaction = wallet.createTransaction(recipient, amount, bc, tp);
   p2pServer.broadcastTransaction(transaction);
   res.redirect('/transactions');
 });

// app.get('/Login', (req, res) => {
//   // Render the login form or page
//   res.sendFile(path.join(__dirname, 'login.html'));
// });

// app.post('/Login', (req, res) => {
//   const { recipient, amount } = req.body;
//   const transaction = wallet.createTransaction(recipient, amount, bc, tp);
//   p2pServer.broadcastTransaction(transaction);
//   res.redirect('/transactions');
// });


app.get('/mine-transactions', (req, res) => {
  const block = miner.mine();
  console.log(`New block added: ${block.toString()}`);
  res.redirect('/blocks');
});

app.get('/public-key', (req, res) => {
  res.json({ publicKey: wallet.publicKey });
});

app.listen(HTTP_PORT, () => console.log(`Listening on port ${HTTP_PORT}`));
p2pServer.listen();