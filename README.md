# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 383
- HTTP: 114 alive / 56 gold
- HTTPS: 45 alive / 9 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
