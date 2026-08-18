# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 265
- HTTP: 210 alive / 32 gold
- HTTPS: 177 alive / 4 gold
- SOCKS4: 196 alive / 119 gold
- SOCKS5: 213 alive / 110 gold

## Historical pool

- Discovered: 99137
- Ever alive: 11879
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
