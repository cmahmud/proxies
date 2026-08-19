# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 467
- HTTP: 383 alive / 120 gold
- HTTPS: 276 alive / 72 gold
- SOCKS4: 237 alive / 136 gold
- SOCKS5: 219 alive / 139 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16565
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
