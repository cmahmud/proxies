# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 395
- HTTP: 167 alive / 62 gold
- HTTPS: 64 alive / 16 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 190 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33513
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
