# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 403
- HTTP: 87 alive / 62 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37619
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
