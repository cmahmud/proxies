# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 411
- HTTP: 228 alive / 89 gold
- HTTPS: 165 alive / 25 gold
- SOCKS4: 205 alive / 141 gold
- SOCKS5: 225 alive / 156 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31965
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
