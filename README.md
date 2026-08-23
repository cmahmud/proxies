# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 202
- HTTP: 131 alive / 44 gold
- HTTPS: 61 alive / 5 gold
- SOCKS4: 98 alive / 68 gold
- SOCKS5: 113 alive / 85 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32755
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
