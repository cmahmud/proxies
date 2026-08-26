# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 411
- HTTP: 110 alive / 66 gold
- HTTPS: 70 alive / 21 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38726
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
