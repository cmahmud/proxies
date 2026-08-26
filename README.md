# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 373
- HTTP: 105 alive / 65 gold
- HTTPS: 65 alive / 16 gold
- SOCKS4: 150 alive / 140 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38779
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
