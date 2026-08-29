# SyndProxy validated proxy pool

## Current pool

- Alive now: 441
- Gold now: 351
- HTTP: 66 alive / 50 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 163 alive / 146 gold
- SOCKS5: 168 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43523
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
