# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 395
- HTTP: 200 alive / 62 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 192 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33513
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
