# SyndProxy validated proxy pool

## Current pool

- Alive now: 372
- Gold now: 348
- HTTP: 39 alive / 31 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 167 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43612
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
