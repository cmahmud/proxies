# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 404
- HTTP: 78 alive / 60 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42800
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
