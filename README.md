# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 388
- HTTP: 114 alive / 59 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33419
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
