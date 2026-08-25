# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 409
- HTTP: 101 alive / 70 gold
- HTTPS: 83 alive / 15 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34834
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
