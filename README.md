# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 350
- HTTP: 104 alive / 82 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 80 alive / 74 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48669
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
