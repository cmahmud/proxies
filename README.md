# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 376
- HTTP: 95 alive / 48 gold
- HTTPS: 54 alive / 11 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33410
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
