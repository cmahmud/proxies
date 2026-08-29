# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 370
- HTTP: 82 alive / 58 gold
- HTTPS: 82 alive / 13 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 172 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43343
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
