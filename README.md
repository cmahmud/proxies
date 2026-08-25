# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 396
- HTTP: 108 alive / 64 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 166 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37384
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
