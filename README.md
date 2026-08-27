# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 401
- HTTP: 85 alive / 57 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 188 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41584
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
