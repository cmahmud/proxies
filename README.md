# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 362
- HTTP: 345 alive / 82 gold
- HTTPS: 265 alive / 19 gold
- SOCKS4: 201 alive / 126 gold
- SOCKS5: 243 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29839
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
