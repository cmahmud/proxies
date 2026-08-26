# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 405
- HTTP: 107 alive / 63 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38727
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
