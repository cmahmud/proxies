# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 421
- HTTP: 103 alive / 71 gold
- HTTPS: 103 alive / 21 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37840
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
