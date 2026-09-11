# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 356
- HTTP: 113 alive / 71 gold
- HTTPS: 47 alive / 22 gold
- SOCKS4: 101 alive / 95 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48702
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
