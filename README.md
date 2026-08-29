# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 379
- HTTP: 78 alive / 52 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43498
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
