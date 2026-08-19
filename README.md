# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 473
- HTTP: 352 alive / 120 gold
- HTTPS: 266 alive / 72 gold
- SOCKS4: 229 alive / 139 gold
- SOCKS5: 216 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16544
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
