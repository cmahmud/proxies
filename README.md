# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 401
- HTTP: 74 alive / 58 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42756
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
