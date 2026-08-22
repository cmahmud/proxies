# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 381
- HTTP: 277 alive / 83 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 167 alive / 107 gold
- SOCKS5: 239 alive / 168 gold

## Historical pool

- Discovered: 166622
- Ever alive: 32455
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
