# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 398
- HTTP: 113 alive / 59 gold
- HTTPS: 85 alive / 11 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38260
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
