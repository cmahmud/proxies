# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 397
- HTTP: 265 alive / 87 gold
- HTTPS: 218 alive / 23 gold
- SOCKS4: 193 alive / 133 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27261
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
