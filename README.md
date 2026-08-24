# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 378
- HTTP: 96 alive / 47 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33411
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
