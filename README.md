# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 473
- HTTP: 382 alive / 120 gold
- HTTPS: 265 alive / 72 gold
- SOCKS4: 233 alive / 139 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16543
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
