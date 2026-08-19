# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 477
- HTTP: 381 alive / 121 gold
- HTTPS: 246 alive / 71 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 247 alive / 142 gold

## Historical pool

- Discovered: 113581
- Ever alive: 16895
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
