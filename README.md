# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 433
- HTTP: 400 alive / 102 gold
- HTTPS: 294 alive / 24 gold
- SOCKS4: 270 alive / 150 gold
- SOCKS5: 260 alive / 157 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25156
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
