# SyndProxy private pool

## Current pool

- Alive now: 1411
- Gold now: 434
- HTTP: 533 alive / 93 gold
- HTTPS: 326 alive / 23 gold
- SOCKS4: 241 alive / 149 gold
- SOCKS5: 311 alive / 169 gold

## Historical pool

- Discovered: 136209
- Ever alive: 22423
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
