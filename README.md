# SyndProxy private pool

## Current pool

- Alive now: 1235
- Gold now: 437
- HTTP: 403 alive / 101 gold
- HTTPS: 306 alive / 30 gold
- SOCKS4: 261 alive / 151 gold
- SOCKS5: 265 alive / 155 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25166
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
