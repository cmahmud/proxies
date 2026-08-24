# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 381
- HTTP: 101 alive / 48 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33411
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
