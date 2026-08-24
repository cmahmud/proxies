# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 383
- HTTP: 111 alive / 56 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
