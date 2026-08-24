# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 384
- HTTP: 98 alive / 56 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
