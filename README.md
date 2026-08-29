# SyndProxy validated proxy pool

## Current pool

- Alive now: 350
- Gold now: 324
- HTTP: 38 alive / 26 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 154 alive / 150 gold
- SOCKS5: 157 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
