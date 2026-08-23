# SyndProxy validated proxy pool

## Current pool

- Alive now: 306
- Gold now: 199
- HTTP: 93 alive / 36 gold
- HTTPS: 30 alive / 6 gold
- SOCKS4: 77 alive / 69 gold
- SOCKS5: 106 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32764
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
