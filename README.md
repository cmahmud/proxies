# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 380
- HTTP: 102 alive / 55 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33413
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
