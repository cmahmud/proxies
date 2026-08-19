# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 342
- HTTP: 334 alive / 65 gold
- HTTPS: 215 alive / 14 gold
- SOCKS4: 244 alive / 141 gold
- SOCKS5: 213 alive / 122 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15323
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
