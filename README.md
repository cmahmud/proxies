# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 432
- HTTP: 142 alive / 79 gold
- HTTPS: 89 alive / 21 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34449
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
