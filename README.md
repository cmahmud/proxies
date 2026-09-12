# SyndProxy validated proxy pool

## Current pool

- Alive now: 367
- Gold now: 305
- HTTP: 82 alive / 60 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 111 alive / 100 gold
- SOCKS5: 139 alive / 124 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49506
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
