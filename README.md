# SyndProxy private pool

## Current pool

- Alive now: 1214
- Gold now: 474
- HTTP: 451 alive / 122 gold
- HTTPS: 281 alive / 72 gold
- SOCKS4: 243 alive / 140 gold
- SOCKS5: 239 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
