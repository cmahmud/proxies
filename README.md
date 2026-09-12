# SyndProxy validated proxy pool

## Current pool

- Alive now: 374
- Gold now: 304
- HTTP: 79 alive / 61 gold
- HTTPS: 35 alive / 20 gold
- SOCKS4: 113 alive / 101 gold
- SOCKS5: 147 alive / 122 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49488
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
