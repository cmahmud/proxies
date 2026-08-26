# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 396
- HTTP: 105 alive / 57 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38974
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
