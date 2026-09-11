# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 351
- HTTP: 107 alive / 79 gold
- HTTPS: 54 alive / 26 gold
- SOCKS4: 80 alive / 74 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48666
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
