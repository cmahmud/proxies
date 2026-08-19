# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 476
- HTTP: 375 alive / 121 gold
- HTTPS: 229 alive / 71 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 249 alive / 141 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16889
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
