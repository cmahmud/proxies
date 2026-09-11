# SyndProxy validated proxy pool

## Current pool

- Alive now: 432
- Gold now: 358
- HTTP: 118 alive / 80 gold
- HTTPS: 44 alive / 28 gold
- SOCKS4: 82 alive / 75 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48654
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
