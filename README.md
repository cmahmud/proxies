# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 405
- HTTP: 119 alive / 62 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38964
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
