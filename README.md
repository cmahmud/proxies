# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 408
- HTTP: 108 alive / 64 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38662
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
