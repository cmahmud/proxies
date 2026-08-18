# SyndProxy private pool

## Current pool

- Alive now: 587
- Gold now: 218
- HTTP: 153 alive / 29 gold
- HTTPS: 83 alive / 8 gold
- SOCKS4: 156 alive / 98 gold
- SOCKS5: 195 alive / 83 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
