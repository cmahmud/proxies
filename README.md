# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 364
- HTTP: 327 alive / 83 gold
- HTTPS: 241 alive / 20 gold
- SOCKS4: 196 alive / 126 gold
- SOCKS5: 249 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29844
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
