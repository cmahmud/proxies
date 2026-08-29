# SyndProxy validated proxy pool

## Current pool

- Alive now: 342
- Gold now: 294
- HTTP: 34 alive / 26 gold
- HTTPS: 2 alive / 1 gold
- SOCKS4: 153 alive / 147 gold
- SOCKS5: 153 alive / 120 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
