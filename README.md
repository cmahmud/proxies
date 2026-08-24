# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 378
- HTTP: 97 alive / 51 gold
- HTTPS: 36 alive / 7 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33407
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
