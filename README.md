# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 473
- HTTP: 463 alive / 122 gold
- HTTPS: 276 alive / 72 gold
- SOCKS4: 244 alive / 140 gold
- SOCKS5: 239 alive / 139 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16521
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
