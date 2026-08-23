# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 345
- HTTP: 126 alive / 38 gold
- HTTPS: 113 alive / 8 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 213 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
