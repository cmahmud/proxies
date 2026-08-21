# SyndProxy private pool

## Current pool

- Alive now: 1275
- Gold now: 423
- HTTP: 485 alive / 97 gold
- HTTPS: 355 alive / 28 gold
- SOCKS4: 200 alive / 140 gold
- SOCKS5: 235 alive / 158 gold

## Historical pool

- Discovered: 159271
- Ever alive: 30398
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
