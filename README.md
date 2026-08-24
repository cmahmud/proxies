# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 391
- HTTP: 97 alive / 60 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 186 alive / 156 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
