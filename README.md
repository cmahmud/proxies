# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 323
- HTTP: 74 alive / 61 gold
- HTTPS: 29 alive / 5 gold
- SOCKS4: 146 alive / 133 gold
- SOCKS5: 166 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
