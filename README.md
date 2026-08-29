# SyndProxy validated proxy pool

## Current pool

- Alive now: 350
- Gold now: 308
- HTTP: 39 alive / 22 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 153 alive / 148 gold
- SOCKS5: 157 alive / 138 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43620
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
