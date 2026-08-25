# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 403
- HTTP: 88 alive / 62 gold
- HTTPS: 81 alive / 21 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37622
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
