# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 404
- HTTP: 228 alive / 92 gold
- HTTPS: 137 alive / 21 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 213 alive / 151 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27760
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
