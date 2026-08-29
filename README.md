# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 349
- HTTP: 45 alive / 33 gold
- HTTPS: 10 alive / 1 gold
- SOCKS4: 158 alive / 156 gold
- SOCKS5: 166 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43602
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
