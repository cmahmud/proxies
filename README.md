# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 394
- HTTP: 95 alive / 63 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 161 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37512
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
