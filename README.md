# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 396
- HTTP: 74 alive / 54 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42760
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
