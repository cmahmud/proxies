# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 403
- HTTP: 105 alive / 62 gold
- HTTPS: 68 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38408
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
