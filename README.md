# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 397
- HTTP: 261 alive / 85 gold
- HTTPS: 220 alive / 24 gold
- SOCKS4: 199 alive / 132 gold
- SOCKS5: 208 alive / 156 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27251
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
