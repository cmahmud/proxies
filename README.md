# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 374
- HTTP: 81 alive / 44 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 172315
- Ever alive: 32972
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
