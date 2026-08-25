# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 395
- HTTP: 110 alive / 64 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 166 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37387
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
