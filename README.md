# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 403
- HTTP: 91 alive / 62 gold
- HTTPS: 89 alive / 21 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37626
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
