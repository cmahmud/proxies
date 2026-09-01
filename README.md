# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 403
- HTTP: 75 alive / 49 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47104
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
