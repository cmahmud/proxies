# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 312
- HTTP: 82 alive / 60 gold
- HTTPS: 36 alive / 21 gold
- SOCKS4: 117 alive / 102 gold
- SOCKS5: 141 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49513
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
