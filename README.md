# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 292
- HTTP: 108 alive / 75 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 75 alive / 64 gold
- SOCKS5: 157 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47897
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
