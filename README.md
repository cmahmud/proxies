# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 433
- HTTP: 133 alive / 78 gold
- HTTPS: 89 alive / 25 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34612
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
