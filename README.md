# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 399
- HTTP: 100 alive / 59 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
