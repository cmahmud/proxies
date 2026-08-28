# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 389
- HTTP: 106 alive / 72 gold
- HTTPS: 66 alive / 13 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 168 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43125
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
