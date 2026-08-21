# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 373
- HTTP: 246 alive / 81 gold
- HTTPS: 149 alive / 25 gold
- SOCKS4: 208 alive / 130 gold
- SOCKS5: 228 alive / 137 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29353
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
