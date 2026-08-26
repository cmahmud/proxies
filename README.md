# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 403
- HTTP: 98 alive / 61 gold
- HTTPS: 80 alive / 14 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39278
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
