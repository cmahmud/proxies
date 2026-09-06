# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 305
- HTTP: 73 alive / 49 gold
- HTTPS: 30 alive / 8 gold
- SOCKS4: 149 alive / 133 gold
- SOCKS5: 143 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48330
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
