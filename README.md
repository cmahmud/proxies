# SyndProxy validated proxy pool

## Current pool

- Alive now: 344
- Gold now: 315
- HTTP: 40 alive / 25 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 150 alive / 148 gold
- SOCKS5: 151 alive / 142 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
