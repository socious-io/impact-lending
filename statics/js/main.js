import Web3 from 'web3';
import axios from 'axios';
import {
  EthereumClient,
  w3mConnectors,
  w3mProvider,
} from "@web3modal/ethereum";
import { Web3Modal } from "@web3modal/html";
import { configureChains, createConfig } from "@wagmi/core";
import { getAccount, watchAccount } from '@wagmi/core'
import { dappConfig } from './dapp.config'
import {walletConnectedView, walletDisconnectedView} from './view'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

let web3;
let connected = false;
const networks = process.env.DAPP_ENV === 'mainet' ? dappConfig.mainet : dappConfig.testnet;
const projectId = dappConfig.walletConnetProjectId;
const chains = networks.map((n) => n.chain);


const { publicClient } = configureChains(chains, [w3mProvider({ projectId })]);
const wagmiConfig = createConfig({
  autoConnect: true,
  connectors: w3mConnectors({ projectId, version: 1, chains }),
  publicClient,
});

const ethereumClient = new EthereumClient(wagmiConfig, chains);
const web3modal = new Web3Modal({ projectId }, ethereumClient);

const connectDiv = document.getElementById("wallet-connect");
const createProjectBtn = document.getElementById("create-project")

const connect = async (account) => {
  const provider = await account.connector.getProvider();
  web3 = new Web3(provider);
  connected = true;
  if (connectDiv) {
    connectDiv.innerHTML = walletConnectedView(account.address);
    document.getElementById("wallet-connect-btn")?.addEventListener("click", () => {
      web3modal.openModal()
    });
    if (createProjectBtn) createProjectBtn.disabled = false;
  }
}

const disconnect = async () => {
  connected = false;
  if (connectDiv) {
    connectDiv.innerHTML = walletDisconnectedView;
    document.getElementById("wallet-connect-btn")?.addEventListener("click", () => {
      web3modal.openModal()
    });  
    if (createProjectBtn) createProjectBtn.disabled = true;
  }
}

watchAccount(async (account) => {
  account?.isConnected ? await connect(account) : await disconnect();
});




createProjectBtn?.addEventListener("click", async () => {
  const account = getAccount();
  if (!account.isConnected) return alert('Please connect your wallet first');
  const dataset = document.getElementById("project-data");
  const id = dataset.getAttribute('data-id');
  const amount = dataset.getAttribute('data-amount');

  const contract = new web3.eth.Contract(dappConfig.abis.lending, networks[0].contract);

  try {
    await contract.methods
      .createProject(id, amount, networks[0].tokens[0].address)
      .send({from: account.address});
  } catch(err) {
    return alert(err);
  }

  try {
    await axios.post('/projects/create/3');
  } catch {
    return alert('server fault');
  }
  window.location = '/projects/list';
});


document.getElementById("lend-action")?.addEventListener("click", async () => {  
  const account = getAccount();
  if (!account.isConnected) return alert('Please connect your wallet first');
  const dataset = document.getElementById("project-data");
  const id = dataset.getAttribute('data-id');
  const reachGoalAmount = dataset.getAttribute('data-reach-goal-amount');
  const lendAmount = document.getElementById("lend-amount")?.value;

  if (!lendAmount || parseInt(lendAmount) > parseInt(reachGoalAmount)) {
    return alert('lending amount is not valid');
  }

  const amount = web3.utils.toWei(lendAmount);

  const contract = new web3.eth.Contract(dappConfig.abis.lending, networks[0].contract);
  const tokenContract = new web3.eth.Contract(dappConfig.abis.token, networks[0].tokens[0].address);
  
  let txHash = '';

  try {
    await tokenContract.methods
      .approve(networks[0].contract, amount)
      .send({ from: account.address });


    const trx = await contract.methods
      .lending(id, amount)
      .send({from: account.address});
      
    txHash = trx.transactionHash;

  } catch(err) {
    return alert(err.toString());
  }

  try {
    await axios.post(`/projects/${id}/lend`, {
      source: account.address,
      amount: lendAmount,
      tx_hash: txHash
    });
  } catch {
    return alert('could not verify transaction');
  }
  
  window.location = `/projects/${id}`;

})

document.getElementById("borrow-action")?.addEventListener("click", async () => {  
  const account = getAccount();
  if (!account.isConnected) return alert('Please connect your wallet first');
  const dataset = document.getElementById("project-data");
  const id = dataset.getAttribute('data-id');
  const reachGoalAmount = dataset.getAttribute('data-reach-goal-amount');
  const lendAmount = document.getElementById("lend-amount")?.value;

  if (parseInt(reachGoalAmount) != 0) {
    return alert('Withrawn action is not valid');
  }


  const contract = new web3.eth.Contract(dappConfig.abis.lending, networks[0].contract);

  let txHash = '';

  try {

    const trx = await contract.methods
      .borrow(id)
      .send({from: account.address});
      
    txHash = trx.transactionHash;

  } catch(err) {
    return alert(err.toString());
  }

  try {
    await axios.post(`/projects/${id}/withdrawn`, {
      source: networks[0].contract,
      dest: account.address,
      amount: lendAmount,
      tx_hash: txHash
    });
  } catch {
    return alert('could not verify transaction');
  }
  
  window.location = `/projects/${id}`;

})



document.getElementById('photos')?.addEventListener('change', function(e){
  let preview = document.getElementById('photo-preview');
  preview.innerHTML = '';
  let files = e.target.files;
  for(let i = 0; i < files.length; i++){
      let file = files[i];
      let img = document.createElement('img');
      img.src = URL.createObjectURL(file);
      img.style.width = '30%';
      img.onload = function() {
          URL.revokeObjectURL(this.src);
      }
      preview.appendChild(img);
  }
});
