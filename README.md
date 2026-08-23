# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 369
- HTTP: 90 alive / 50 gold
- HTTPS: 44 alive / 11 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33041
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
