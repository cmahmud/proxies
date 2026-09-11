# SyndProxy validated proxy pool

## Current pool

- Alive now: 436
- Gold now: 360
- HTTP: 121 alive / 84 gold
- HTTPS: 39 alive / 26 gold
- SOCKS4: 83 alive / 76 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48647
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
