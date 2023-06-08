export const walletConnectedView = (address) => `
<div class="section-form">
  <div class="connect-wallet-step2-form">
    <div class="connect-wallet-step2-formfields">
      <div class="card">
        <div class="connect-wallet-step2-inputfield">
          <div class="connect-wallet-step2-inputwithlabel">
            <span
              class="connect-wallet-step2-text02 TextsmMedium"
            >
              <span>Your wallet address</span>
            </span>
            <div class="connect-wallet-step2-input">
              <div class="connect-wallet-step2-content">
                <input
                  type="text"
                  disabled=disabled
                  value=${address}
                  class="connect-wallet-step2-textinput TextmdRegular"
                />
              </div>
              <button class="connect-wallet-step2-button">
                <img
                  alt="copy01I763"
                  src="/statics/img/copy01i763-vilj.svg"
                  class="connect-wallet-step2-copy01"
                />
                <span
                  class="connect-wallet-step2-text04 TextsmSemibold"
                >
                  <span>Copy</span>
                </span>
              </button>
            </div>
          </div>
          <span class="connect-wallet-step2-text06 TextsmRegular">
            <span>
              This is the address where you will receive your loan
              once your project is funded
            </span>
          </span>
        </div>
        <button class="connect-wallet-step2-button1" id="wallet-connect-btn">
          <span
            class="connect-wallet-step2-text08 TextmdSemibold"
          >
            <span>Disconnect wallet</span>
          </span>
        </button>
      </div>
    </div>
  </div>
</div>
`
export const walletDisconnectedView = `
<div class="connect-wallet-step1-actions">
  <span class="connect-wallet-step1-text1 TextlgRegular">
    There is not wallet connected to your account.
  </span>
  <button class="connect-wallet-step1-walletbutton button-secondary-gray" id="wallet-connect-btn">
    <div class="connect-wallet-step1-walleticon">
      <div class="connect-wallet-step1-group">
        <img
          alt="VectorI763"
          src="/statics/img/vectori763-p3z9.svg"
          class="connect-wallet-step1-vector"
        />
        <img
          alt="VectorI763"
          src="/statics/img/vectori763-vdy.svg"
          class="connect-wallet-step1-vector1"
        />
      </div>
    </div>
    <span class="connect-wallet-step1-text2 TextmdSemibold">
      <span>WalletConnect</span>
    </span>
  </button>
</div>
`
