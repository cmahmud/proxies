# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 373
- HTTP: 97 alive / 49 gold
- HTTPS: 35 alive / 6 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33408
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
