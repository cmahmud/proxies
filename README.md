# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 446
- HTTP: 318 alive / 112 gold
- HTTPS: 233 alive / 30 gold
- SOCKS4: 226 alive / 156 gold
- SOCKS5: 243 alive / 148 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30526
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
