# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 321
- HTTP: 289 alive / 43 gold
- HTTPS: 168 alive / 10 gold
- SOCKS4: 233 alive / 138 gold
- SOCKS5: 220 alive / 130 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14290
- Ever gold: 439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
