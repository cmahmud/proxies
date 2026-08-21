# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 397
- HTTP: 266 alive / 88 gold
- HTTPS: 179 alive / 24 gold
- SOCKS4: 227 alive / 147 gold
- SOCKS5: 231 alive / 138 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29373
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
