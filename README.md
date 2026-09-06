# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 312
- HTTP: 76 alive / 48 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 142 alive / 134 gold
- SOCKS5: 142 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48321
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
