# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 476
- HTTP: 377 alive / 120 gold
- HTTPS: 230 alive / 72 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 250 alive / 142 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16888
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
