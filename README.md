# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 350
- HTTP: 80 alive / 61 gold
- HTTPS: 33 alive / 15 gold
- SOCKS4: 153 alive / 139 gold
- SOCKS5: 167 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
