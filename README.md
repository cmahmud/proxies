# SyndProxy private pool

## Current pool

- Alive now: 1169
- Gold now: 472
- HTTP: 412 alive / 120 gold
- HTTPS: 270 alive / 76 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 253 alive / 135 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16483
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
