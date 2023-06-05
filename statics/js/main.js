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

const connectBtn = document.getElementById("wallet-connect");

const connect = async (account) => {
  const provider = await account.connector.getProvider();
  web3 = new Web3(provider);
  connected = true;
  connectBtn.textContent = 'disconnect'
}

const disconnect = async () => {
  connected = false;
  connectBtn.textContent = 'connect'
}

watchAccount(async (account) => {
  account?.isConnected ? await connect(account) : await disconnect();
});

connectBtn.addEventListener("click", () => {
  web3modal.openModal();
});



document.getElementById("create-project").addEventListener("click", async () => {
  const account = getAccount();
  if (!account.isConnected) return alert('Please connect your wallet first');
  const dataset = document.getElementById("project-data");
  const id = dataset.getAttribute('data-id');
  const amount = dataset.getAttribute('data-amount');

  const contract = new web3.eth.Contract(dappConfig.abis.lending, networks[0].contract);
  await contract.methods
    .createProject(id, amount, networks[0].tokens[0].address)
    .send({from: account.address});

  const response = await axios.post('/projects/create/3')
  if (response.status == 200) window.location = '/projects/list'
});


document.getElementById("lend-action").addEventListener("click", async () => {
  document.getElementById("lend-amount");
})
