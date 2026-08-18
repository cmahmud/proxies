# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 303
- HTTP: 379 alive / 28 gold
- HTTPS: 149 alive / 5 gold
- SOCKS4: 229 alive / 142 gold
- SOCKS5: 218 alive / 128 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13349
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
