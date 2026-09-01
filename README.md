# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 444
- HTTP: 108 alive / 79 gold
- HTTPS: 93 alive / 31 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47009
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
