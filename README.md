# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 342
- HTTP: 304 alive / 68 gold
- HTTPS: 251 alive / 18 gold
- SOCKS4: 235 alive / 141 gold
- SOCKS5: 231 alive / 115 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16104
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
