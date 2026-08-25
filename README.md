# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 402
- HTTP: 98 alive / 69 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 165 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37454
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
