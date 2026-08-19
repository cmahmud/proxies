# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 473
- HTTP: 364 alive / 120 gold
- HTTPS: 265 alive / 72 gold
- SOCKS4: 238 alive / 139 gold
- SOCKS5: 223 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16544
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
