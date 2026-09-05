# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 293
- HTTP: 106 alive / 75 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 77 alive / 67 gold
- SOCKS5: 156 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47863
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
