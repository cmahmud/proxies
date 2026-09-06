# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 304
- HTTP: 69 alive / 47 gold
- HTTPS: 26 alive / 7 gold
- SOCKS4: 143 alive / 132 gold
- SOCKS5: 141 alive / 118 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48325
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
