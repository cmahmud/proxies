# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 377
- HTTP: 101 alive / 52 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33412
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
