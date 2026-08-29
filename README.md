# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 391
- HTTP: 89 alive / 62 gold
- HTTPS: 51 alive / 21 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43649
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
