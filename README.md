# SyndProxy validated proxy pool

## Current pool

- Alive now: 350
- Gold now: 279
- HTTP: 39 alive / 22 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 154 alive / 132 gold
- SOCKS5: 152 alive / 124 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
