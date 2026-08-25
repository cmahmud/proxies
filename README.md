# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 395
- HTTP: 82 alive / 65 gold
- HTTPS: 65 alive / 16 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 168 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37265
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
