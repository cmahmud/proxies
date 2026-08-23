# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 202
- HTTP: 131 alive / 44 gold
- HTTPS: 62 alive / 5 gold
- SOCKS4: 94 alive / 67 gold
- SOCKS5: 114 alive / 86 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32754
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
