# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 200
- HTTP: 140 alive / 43 gold
- HTTPS: 49 alive / 5 gold
- SOCKS4: 92 alive / 67 gold
- SOCKS5: 118 alive / 85 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32753
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
