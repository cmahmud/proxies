# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 421
- HTTP: 94 alive / 71 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 200 alive / 166 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49077
- Ever gold: 1571

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
