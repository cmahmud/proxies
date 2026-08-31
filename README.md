# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 477
- HTTP: 154 alive / 105 gold
- HTTPS: 150 alive / 37 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
