# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 397
- HTTP: 350 alive / 107 gold
- HTTPS: 268 alive / 25 gold
- SOCKS4: 206 alive / 143 gold
- SOCKS5: 220 alive / 122 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28499
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
