# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 402
- HTTP: 101 alive / 66 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 168 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37285
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
