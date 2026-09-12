# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 312
- HTTP: 85 alive / 60 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 113 alive / 104 gold
- SOCKS5: 139 alive / 126 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49508
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
