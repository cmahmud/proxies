# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 380
- HTTP: 70 alive / 52 gold
- HTTPS: 67 alive / 13 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43503
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
