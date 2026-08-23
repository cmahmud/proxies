# SyndProxy validated proxy pool

## Current pool

- Alive now: 404
- Gold now: 201
- HTTP: 142 alive / 43 gold
- HTTPS: 53 alive / 6 gold
- SOCKS4: 90 alive / 67 gold
- SOCKS5: 119 alive / 85 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32753
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
