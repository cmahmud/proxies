# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 295
- HTTP: 300 alive / 35 gold
- HTTPS: 199 alive / 6 gold
- SOCKS4: 222 alive / 129 gold
- SOCKS5: 217 alive / 125 gold

## Historical pool

- Discovered: 102845
- Ever alive: 13205
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
