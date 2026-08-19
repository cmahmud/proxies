# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 324
- HTTP: 272 alive / 64 gold
- HTTPS: 229 alive / 19 gold
- SOCKS4: 227 alive / 127 gold
- SOCKS5: 207 alive / 114 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15391
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
