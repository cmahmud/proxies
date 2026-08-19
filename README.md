# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 373
- HTTP: 349 alive / 73 gold
- HTTPS: 195 alive / 18 gold
- SOCKS4: 212 alive / 125 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15792
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
