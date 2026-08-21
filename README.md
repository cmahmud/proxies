# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 403
- HTTP: 345 alive / 98 gold
- HTTPS: 258 alive / 33 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 218 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30297
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
