# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 408
- HTTP: 99 alive / 61 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38430
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
