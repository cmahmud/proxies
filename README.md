# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 342
- HTTP: 98 alive / 39 gold
- HTTPS: 52 alive / 10 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 168 alive / 143 gold

## Historical pool

- Discovered: 171059
- Ever alive: 32858
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
