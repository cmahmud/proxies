# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 274
- HTTP: 441 alive / 24 gold
- HTTPS: 211 alive / 5 gold
- SOCKS4: 218 alive / 124 gold
- SOCKS5: 230 alive / 121 gold

## Historical pool

- Discovered: 102838
- Ever alive: 13053
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
