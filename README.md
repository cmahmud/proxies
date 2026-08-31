# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 427
- HTTP: 94 alive / 69 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45484
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
