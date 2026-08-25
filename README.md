# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 400
- HTTP: 99 alive / 63 gold
- HTTPS: 85 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37568
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
