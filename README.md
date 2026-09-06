# SyndProxy validated proxy pool

## Current pool

- Alive now: 430
- Gold now: 352
- HTTP: 83 alive / 62 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 149 alive / 136 gold
- SOCKS5: 165 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
