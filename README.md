# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 377
- HTTP: 97 alive / 49 gold
- HTTPS: 47 alive / 9 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33409
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
