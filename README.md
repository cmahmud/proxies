# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 348
- HTTP: 87 alive / 34 gold
- HTTPS: 63 alive / 10 gold
- SOCKS4: 181 alive / 149 gold
- SOCKS5: 198 alive / 155 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
