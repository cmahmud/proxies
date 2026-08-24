# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 388
- HTTP: 116 alive / 57 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33421
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
