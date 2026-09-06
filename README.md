# SyndProxy validated proxy pool

## Current pool

- Alive now: 398
- Gold now: 323
- HTTP: 74 alive / 51 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 148 alive / 134 gold
- SOCKS5: 145 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48335
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
