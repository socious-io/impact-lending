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
      contract: 'LENDING SMART CONTRACT',
      tokens: [
        {
          name: 'USDC',
          symbol: 'USDC',
          address: '0x95cEc3b0a113AEf23eaFA4eD1B48489806bF6C82',
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
    lending:[],
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
