# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 423
- HTTP: 111 alive / 76 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37915
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
