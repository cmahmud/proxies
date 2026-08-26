# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 405
- HTTP: 113 alive / 62 gold
- HTTPS: 77 alive / 15 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38410
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
