# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 387
- HTTP: 120 alive / 56 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 192 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33423
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
