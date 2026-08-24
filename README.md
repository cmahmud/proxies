# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 393
- HTTP: 98 alive / 58 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33352
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
