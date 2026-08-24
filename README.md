# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 384
- HTTP: 89 alive / 59 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 176 alive / 158 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
