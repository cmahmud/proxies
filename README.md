# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 408
- HTTP: 121 alive / 61 gold
- HTTPS: 149 alive / 19 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41317
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
