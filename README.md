# SyndProxy validated proxy pool

## Current pool

- Alive now: 405
- Gold now: 199
- HTTP: 132 alive / 42 gold
- HTTPS: 58 alive / 5 gold
- SOCKS4: 98 alive / 67 gold
- SOCKS5: 117 alive / 85 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32754
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
