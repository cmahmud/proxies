# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 236
- HTTP: 293 alive / 33 gold
- HTTPS: 217 alive / 9 gold
- SOCKS4: 245 alive / 113 gold
- SOCKS5: 219 alive / 81 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
