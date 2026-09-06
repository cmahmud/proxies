# SyndProxy validated proxy pool

## Current pool

- Alive now: 436
- Gold now: 342
- HTTP: 85 alive / 58 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 156 alive / 136 gold
- SOCKS5: 163 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48395
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
