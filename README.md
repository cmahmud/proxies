# SyndProxy private pool

## Current pool

- Alive now: 1513
- Gold now: 619
- HTTP: 582 alive / 222 gold
- HTTPS: 475 alive / 113 gold
- SOCKS4: 206 alive / 138 gold
- SOCKS5: 250 alive / 146 gold

## Historical pool

- Discovered: 141135
- Ever alive: 23812
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
