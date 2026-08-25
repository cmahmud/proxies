# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 389
- HTTP: 99 alive / 62 gold
- HTTPS: 72 alive / 16 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 165 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37401
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
