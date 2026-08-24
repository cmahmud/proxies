# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 379
- HTTP: 106 alive / 55 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33413
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
