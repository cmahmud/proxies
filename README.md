# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 375
- HTTP: 105 alive / 67 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 150 alive / 140 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38779
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
