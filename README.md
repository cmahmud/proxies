# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 289
- HTTP: 269 alive / 25 gold
- HTTPS: 150 alive / 4 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 222 alive / 117 gold

## Historical pool

- Discovered: 102825
- Ever alive: 12776
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
