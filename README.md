# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 420
- HTTP: 95 alive / 75 gold
- HTTPS: 104 alive / 20 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42513
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
