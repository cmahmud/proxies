# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 360
- HTTP: 54 alive / 37 gold
- HTTPS: 35 alive / 6 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43581
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
