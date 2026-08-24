# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 391
- HTTP: 104 alive / 60 gold
- HTTPS: 47 alive / 11 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33414
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
