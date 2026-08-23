# SyndProxy validated proxy pool

## Current pool

- Alive now: 314
- Gold now: 200
- HTTP: 98 alive / 38 gold
- HTTPS: 31 alive / 6 gold
- SOCKS4: 79 alive / 67 gold
- SOCKS5: 106 alive / 89 gold

## Historical pool

- Discovered: 170538
- Ever alive: 32764
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
