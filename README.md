# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 375
- HTTP: 70 alive / 49 gold
- HTTPS: 62 alive / 9 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43503
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
