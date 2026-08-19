# SyndProxy private pool

## Current pool

- Alive now: 1210
- Gold now: 496
- HTTP: 426 alive / 121 gold
- HTTPS: 289 alive / 73 gold
- SOCKS4: 246 alive / 152 gold
- SOCKS5: 249 alive / 150 gold

## Historical pool

- Discovered: 113538
- Ever alive: 16585
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
