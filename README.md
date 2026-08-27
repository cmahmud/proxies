# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 405
- HTTP: 100 alive / 61 gold
- HTTPS: 127 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41328
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
