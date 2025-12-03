import requests, time

def telos_burn():
    print("Telos EVM — Burn Ritual Detected (> 1M TLOS sent to 0xdead)")
    seen = set()
    while True:
        r = requests.get("https://api.teloscan.io/api?module=account&action=txlist"
                        "&address=0x000000000000000000000000000000000000dead&sort=desc")
        for tx in r.json().get("result", [])[:40]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Transfer to 0xdead = intentional burn on Telos EVM
            if tx["to"].lower() != "0x000000000000000000000000000000000000dead": continue
            if tx.get("contractAddress"): continue

            value = int(tx["value"]) / 1e18
            if value >= 1_000_000:  # > 1 million TLOS burned forever
                print(f"BURN RITUAL COMPLETE\n"
                      f"{value:,.0f} TLOS sacrificed to the void\n"
                      f"From: {tx['from']}\n"
                      f"Tx: https://teloscan.io/tx/{h}\n"
                      f"→ Permanent supply reduction\n"
                      f"→ Usually team, foundation, or ultra-bull move\n"
                      f"→ Telos just became more scarce\n"
                      f"{'-'*80}")
        time.sleep(3.1)

if __name__ == "__main__":
    telos_burn()
