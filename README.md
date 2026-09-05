# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 423
- HTTP: 90 alive / 72 gold
- HTTPS: 78 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 209396
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
