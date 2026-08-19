# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 535
- HTTP: 388 alive / 162 gold
- HTTPS: 264 alive / 92 gold
- SOCKS4: 207 alive / 138 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 122387
- Ever alive: 18676
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
