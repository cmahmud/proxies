# SyndProxy private pool

## Current pool

- Alive now: 1291
- Gold now: 593
- HTTP: 491 alive / 179 gold
- HTTPS: 343 alive / 113 gold
- SOCKS4: 233 alive / 145 gold
- SOCKS5: 224 alive / 156 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19545
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
