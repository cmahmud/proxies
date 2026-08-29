# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 363
- HTTP: 55 alive / 43 gold
- HTTPS: 37 alive / 4 gold
- SOCKS4: 161 alive / 155 gold
- SOCKS5: 170 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43546
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
