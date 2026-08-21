# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 356
- HTTP: 295 alive / 77 gold
- HTTPS: 213 alive / 17 gold
- SOCKS4: 196 alive / 127 gold
- SOCKS5: 248 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29846
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
