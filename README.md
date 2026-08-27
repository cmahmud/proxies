# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 405
- HTTP: 112 alive / 61 gold
- HTTPS: 133 alive / 14 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41342
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
