# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 389
- HTTP: 141 alive / 62 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 192 alive / 160 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33132
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
