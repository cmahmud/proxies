# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 416
- HTTP: 114 alive / 67 gold
- HTTPS: 131 alive / 18 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41337
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
