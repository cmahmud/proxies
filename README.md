# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 389
- HTTP: 119 alive / 61 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33419
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
