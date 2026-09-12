# SyndProxy validated proxy pool

## Current pool

- Alive now: 391
- Gold now: 331
- HTTP: 79 alive / 64 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 131 alive / 116 gold
- SOCKS5: 148 alive / 134 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49549
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
