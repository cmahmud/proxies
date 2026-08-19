# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 373
- HTTP: 309 alive / 73 gold
- HTTPS: 191 alive / 18 gold
- SOCKS4: 206 alive / 125 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15791
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
