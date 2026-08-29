# SyndProxy validated proxy pool

## Current pool

- Alive now: 360
- Gold now: 319
- HTTP: 49 alive / 30 gold
- HTTPS: 14 alive / 0 gold
- SOCKS4: 147 alive / 145 gold
- SOCKS5: 150 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43631
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
