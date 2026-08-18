# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 258
- HTTP: 376 alive / 28 gold
- HTTPS: 178 alive / 5 gold
- SOCKS4: 204 alive / 119 gold
- SOCKS5: 217 alive / 106 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11776
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
