# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 388
- HTTP: 116 alive / 57 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33422
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
