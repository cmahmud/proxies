# SyndProxy validated proxy pool

## Current pool

- Alive now: 344
- Gold now: 318
- HTTP: 36 alive / 25 gold
- HTTPS: 4 alive / 1 gold
- SOCKS4: 151 alive / 150 gold
- SOCKS5: 153 alive / 142 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
