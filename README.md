# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 374
- HTTP: 59 alive / 45 gold
- HTTPS: 40 alive / 8 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43542
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
