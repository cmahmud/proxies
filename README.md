# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 387
- HTTP: 94 alive / 66 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 172 alive / 130 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48756
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
