const milkomedaTestnet = {
  id: 200101,
  name: 'Milkomeda Testnet',
  network: 'Milkomeda',
  nativeCurrency: {
    name: 'MILKTADA',
    symbol: 'MILKTADA',
    decimals: 18,
  },
  rpcUrls: {
    default: {
      http: ['https://rpc-devnet-cardano-evm.c1.milkomeda.com'],
    },
    public: {
      http: ['https://rpc-devnet-cardano-evm.c1.milkomeda.com'],
    },
  },
  blockExplorers: {
    default: {
      name: 'Explorer',
      url: 'https://explorer-devnet-cardano-evm.c1.milkomeda.com',
    },
  },
  testnet: true,
};

const milkomeda = {
  id: 2002,
  name: 'Milkomeda',
  network: 'Milkomeda',
  nativeCurrency: {
    name: 'MILKADA',
    symbol: 'MILKADA',
    decimals: 18,
  },
  rpcUrls: {
    default: {
      http: ['https://rpc-mainnet-algorand-rollup.a1.milkomeda.com'],
    },
    public: {
      http: ['https://rpc-mainnet-algorand-rollup.a1.milkomeda.com'],
    },
  },
  blockExplorers: {
    default: {
      name: 'Explorer',
      url: 'https://explorer-mainnet-algorand-rollup.a1.milkomeda.com',
    },
  },
};


export const dappConfig= {
  walletConnetProjectId: '40ce0f320baccb067909071c983ca357',
  testnet: [
    {
      chain: milkomedaTestnet,
      contract: '0x99E4D5E1e5C19fbf7c671445BDcc1C8C2aa99885',
      tokens: [
        {
          name: 'USDC',
          symbol: 'USDC',
          address: '0xaa17B7F93fC67a72a8FeF86b02C8A2b330125dAA',
        },
      ],
    },
  ],
  mainet: [
    {
      chain: milkomeda,
      contract: 'LENDING SMART CONTRACT',
      tokens: [
        {
          name: 'USD Coin',
          symbol: 'USDC',
          address: '0xB44a9B6905aF7c801311e8F4E76932ee959c663C',
        },
        {
          name: 'Tether',
          symbol: 'USDT',
          address: '0x80A16016cC4A2E6a2CACA8a4a498b1699fF0f844',
        },
        {
          name: 'Dai',
          symbol: 'DAI',
          address: '0x639A647fbe20b6c8ac19E48E2de44ea792c62c5C',
        },
        {
          name: 'Djed',
          symbol: 'SC',
          address: '0xbfB54440448e6b702fa2A1d7033cd5fB0d9C5A27',
        },
        {
          name: 'Wrapped ADA',
          symbol: 'WADA',
          address: '0xAE83571000aF4499798d1e3b0fA0070EB3A3E3F9',
        },
      ],
    },
  ],

  abis: {
    lending: [
      {
        "anonymous": false,
        "inputs": [
          {
            "indexed": false,
            "internalType": "string",
            "name": "projectId",
            "type": "string"
          },
          {
            "indexed": false,
            "internalType": "address",
            "name": "borrower",
            "type": "address"
          },
          {
            "indexed": false,
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
          }
        ],
        "name": "BorrowAction",
        "type": "event"
      },
      {
        "anonymous": false,
        "inputs": [
          {
            "indexed": false,
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
          },
          {
            "indexed": false,
            "internalType": "string",
            "name": "projectId",
            "type": "string"
          },
          {
            "indexed": false,
            "internalType": "address",
            "name": "lenderAddress",
            "type": "address"
          }
        ],
        "name": "LoanAction",
        "type": "event"
      },
      {
        "anonymous": false,
        "inputs": [
          {
            "indexed": true,
            "internalType": "address",
            "name": "previousOwner",
            "type": "address"
          },
          {
            "indexed": true,
            "internalType": "address",
            "name": "newOwner",
            "type": "address"
          }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
      },
      {
        "anonymous": false,
        "inputs": [
          {
            "indexed": false,
            "internalType": "string",
            "name": "projectId",
            "type": "string"
          },
          {
            "indexed": false,
            "internalType": "address",
            "name": "owner",
            "type": "address"
          },
          {
            "indexed": false,
            "internalType": "uint256",
            "name": "goalAmount",
            "type": "uint256"
          },
          {
            "indexed": false,
            "internalType": "contract IERC20",
            "name": "token",
            "type": "address"
          }
        ],
        "name": "ProjectCreateAction",
        "type": "event"
      },
      {
        "inputs": [
          {
            "internalType": "contract IERC20",
            "name": "_token",
            "type": "address"
          }
        ],
        "name": "addToken",
        "outputs": [
          {
            "internalType": "bool",
            "name": "",
            "type": "bool"
          }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "string",
            "name": "_projectId",
            "type": "string"
          }
        ],
        "name": "borrow",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "string",
            "name": "_projectId",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "_goalAmount",
            "type": "uint256"
          },
          {
            "internalType": "contract IERC20",
            "name": "_token",
            "type": "address"
          }
        ],
        "name": "createProject",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "string",
            "name": "_projectId",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "_amount",
            "type": "uint256"
          }
        ],
        "name": "lending",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "address",
            "name": "newOwner",
            "type": "address"
          }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
      },
      {
        "inputs": [
          {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
          }
        ],
        "name": "borrowHistory",
        "outputs": [
          {
            "internalType": "string",
            "name": "projectId",
            "type": "string"
          },
          {
            "internalType": "address",
            "name": "borrower",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
          }
        ],
        "name": "lendingHistory",
        "outputs": [
          {
            "internalType": "address",
            "name": "lenderAddress",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "projectId",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "owner",
        "outputs": [
          {
            "internalType": "address",
            "name": "",
            "type": "address"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
          }
        ],
        "name": "projects",
        "outputs": [
          {
            "internalType": "string",
            "name": "id",
            "type": "string"
          },
          {
            "internalType": "address",
            "name": "owner",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "goalAmount",
            "type": "uint256"
          },
          {
            "internalType": "enum Lending.Status",
            "name": "status",
            "type": "uint8"
          },
          {
            "internalType": "contract IERC20",
            "name": "token",
            "type": "address"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
          }
        ],
        "name": "validTokens",
        "outputs": [
          {
            "internalType": "contract IERC20",
            "name": "",
            "type": "address"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "version",
        "outputs": [
          {
            "internalType": "string",
            "name": "",
            "type": "string"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      }
    ],
    token: [
      {
        constant: true,
        inputs: [],
        name: 'name',
        outputs: [
          {
            name: '',
            type: 'string',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        constant: false,
        inputs: [
          {
            name: '_spender',
            type: 'address',
          },
          {
            name: '_value',
            type: 'uint256',
          },
        ],
        name: 'approve',
        outputs: [
          {
            name: '',
            type: 'bool',
          },
        ],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'function',
      },
      {
        constant: true,
        inputs: [],
        name: 'totalSupply',
        outputs: [
          {
            name: '',
            type: 'uint256',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        constant: false,
        inputs: [
          {
            name: '_from',
            type: 'address',
          },
          {
            name: '_to',
            type: 'address',
          },
          {
            name: '_value',
            type: 'uint256',
          },
        ],
        name: 'transferFrom',
        outputs: [
          {
            name: '',
            type: 'bool',
          },
        ],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'function',
      },
      {
        constant: true,
        inputs: [],
        name: 'decimals',
        outputs: [
          {
            name: '',
            type: 'uint8',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        constant: true,
        inputs: [
          {
            name: '_owner',
            type: 'address',
          },
        ],
        name: 'balanceOf',
        outputs: [
          {
            name: 'balance',
            type: 'uint256',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        constant: true,
        inputs: [],
        name: 'symbol',
        outputs: [
          {
            name: '',
            type: 'string',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        constant: false,
        inputs: [
          {
            name: '_to',
            type: 'address',
          },
          {
            name: '_value',
            type: 'uint256',
          },
        ],
        name: 'transfer',
        outputs: [
          {
            name: '',
            type: 'bool',
          },
        ],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'function',
      },
      {
        constant: true,
        inputs: [
          {
            name: '_owner',
            type: 'address',
          },
          {
            name: '_spender',
            type: 'address',
          },
        ],
        name: 'allowance',
        outputs: [
          {
            name: '',
            type: 'uint256',
          },
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function',
      },
      {
        payable: true,
        stateMutability: 'payable',
        type: 'fallback',
      },
      {
        anonymous: false,
        inputs: [
          {
            indexed: true,
            name: 'owner',
            type: 'address',
          },
          {
            indexed: true,
            name: 'spender',
            type: 'address',
          },
          {
            indexed: false,
            name: 'value',
            type: 'uint256',
          },
        ],
        name: 'Approval',
        type: 'event',
      },
      {
        anonymous: false,
        inputs: [
          {
            indexed: true,
            name: 'from',
            type: 'address',
          },
          {
            indexed: true,
            name: 'to',
            type: 'address',
          },
          {
            indexed: false,
            name: 'value',
            type: 'uint256',
          },
        ],
        name: 'Transfer',
        type: 'event',
      },
    ],
  },
};
