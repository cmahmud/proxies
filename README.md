# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 202
- HTTP: 121 alive / 44 gold
- HTTPS: 58 alive / 6 gold
- SOCKS4: 91 alive / 67 gold
- SOCKS5: 112 alive / 85 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32755
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
