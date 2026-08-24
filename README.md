# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 388
- HTTP: 105 alive / 60 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 161 alive / 155 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33414
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
