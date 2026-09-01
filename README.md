# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 414
- HTTP: 96 alive / 65 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47036
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
