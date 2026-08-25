# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 405
- HTTP: 93 alive / 66 gold
- HTTPS: 83 alive / 18 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34968
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
