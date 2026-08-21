# SyndProxy private pool

## Current pool

- Alive now: 1210
- Gold now: 428
- HTTP: 442 alive / 107 gold
- HTTPS: 296 alive / 28 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 237 alive / 143 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30514
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
