# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 390
- HTTP: 146 alive / 63 gold
- HTTPS: 38 alive / 13 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 193 alive / 160 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33132
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
