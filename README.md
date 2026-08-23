# SyndProxy validated proxy pool

## Current pool

- Alive now: 363
- Gold now: 205
- HTTP: 112 alive / 45 gold
- HTTPS: 57 alive / 6 gold
- SOCKS4: 83 alive / 66 gold
- SOCKS5: 111 alive / 88 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32755
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
