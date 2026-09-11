# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 348
- HTTP: 102 alive / 78 gold
- HTTPS: 43 alive / 23 gold
- SOCKS4: 82 alive / 76 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48673
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
