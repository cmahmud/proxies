# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 399
- HTTP: 91 alive / 58 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38499
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
