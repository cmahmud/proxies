# SyndProxy validated proxy pool

## Current pool

- Alive now: 421
- Gold now: 353
- HTTP: 79 alive / 64 gold
- HTTPS: 29 alive / 15 gold
- SOCKS4: 150 alive / 137 gold
- SOCKS5: 163 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
