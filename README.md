# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 375
- HTTP: 94 alive / 49 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33410
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
