import Web3 from 'web3';
import {
  EthereumClient,
  w3mConnectors,
  w3mProvider,
} from "@web3modal/ethereum";
import { Web3Modal } from "@web3modal/html";
import { configureChains, createConfig } from "@wagmi/core";
import { getAccount, watchAccount } from '@wagmi/core'
import { dappConfig } from './dapp.config'



let web3;
let connected = false;
const NETWORKS = process.env.DAPP_ENV === 'mainet' ? dappConfig.mainet : dappConfig.testnet;
const projectId = dappConfig.walletConnetProjectId;
const chains = NETWORKS.map((n) => n.chain);


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

document.getElementById("recheck").addEventListener("click", async () => {
  console.log(await web3?.currentProvider, '************');
});
