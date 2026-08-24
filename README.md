# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 391
- HTTP: 111 alive / 57 gold
- HTTPS: 50 alive / 16 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33500
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
