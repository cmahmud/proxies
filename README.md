# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 422
- HTTP: 98 alive / 75 gold
- HTTPS: 112 alive / 19 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42498
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
