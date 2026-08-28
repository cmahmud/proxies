# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 421
- HTTP: 93 alive / 75 gold
- HTTPS: 112 alive / 21 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42513
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
