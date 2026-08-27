# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 410
- HTTP: 100 alive / 67 gold
- HTTPS: 177 alive / 20 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40587
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
