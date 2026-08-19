# SyndProxy private pool

## Current pool

- Alive now: 1401
- Gold now: 418
- HTTP: 518 alive / 91 gold
- HTTPS: 333 alive / 18 gold
- SOCKS4: 258 alive / 152 gold
- SOCKS5: 292 alive / 157 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20863
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
