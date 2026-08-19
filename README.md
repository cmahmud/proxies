# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 477
- HTTP: 380 alive / 121 gold
- HTTPS: 240 alive / 72 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 245 alive / 141 gold

## Historical pool

- Discovered: 113581
- Ever alive: 16895
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
