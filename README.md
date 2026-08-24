# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 385
- HTTP: 102 alive / 53 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33407
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
