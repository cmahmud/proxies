# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 260
- HTTP: 308 alive / 28 gold
- HTTPS: 136 alive / 3 gold
- SOCKS4: 223 alive / 119 gold
- SOCKS5: 222 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12044
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
