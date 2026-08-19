# SyndProxy private pool

## Current pool

- Alive now: 1140
- Gold now: 467
- HTTP: 393 alive / 120 gold
- HTTPS: 284 alive / 72 gold
- SOCKS4: 234 alive / 136 gold
- SOCKS5: 229 alive / 139 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16566
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
