# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 342
- HTTP: 77 alive / 61 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 153 alive / 136 gold
- SOCKS5: 161 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48395
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
