# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 364
- HTTP: 352 alive / 86 gold
- HTTPS: 259 alive / 20 gold
- SOCKS4: 203 alive / 124 gold
- SOCKS5: 239 alive / 134 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29837
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
