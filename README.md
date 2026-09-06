# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 350
- HTTP: 87 alive / 60 gold
- HTTPS: 29 alive / 11 gold
- SOCKS4: 148 alive / 140 gold
- SOCKS5: 170 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48400
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
