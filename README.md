# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 396
- HTTP: 106 alive / 64 gold
- HTTPS: 80 alive / 16 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 166 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37385
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
