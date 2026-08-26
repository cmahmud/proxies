# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 400
- HTTP: 99 alive / 58 gold
- HTTPS: 90 alive / 13 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38203
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
