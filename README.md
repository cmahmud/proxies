# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 358
- HTTP: 119 alive / 85 gold
- HTTPS: 41 alive / 25 gold
- SOCKS4: 82 alive / 76 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48647
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
