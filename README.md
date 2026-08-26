# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 405
- HTTP: 88 alive / 62 gold
- HTTPS: 71 alive / 18 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38598
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
