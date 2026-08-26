# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 408
- HTTP: 113 alive / 65 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38664
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
