# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 326
- HTTP: 79 alive / 63 gold
- HTTPS: 39 alive / 23 gold
- SOCKS4: 120 alive / 109 gold
- SOCKS5: 148 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49500
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
