# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 201
- HTTP: 176 alive / 45 gold
- HTTPS: 63 alive / 6 gold
- SOCKS4: 97 alive / 68 gold
- SOCKS5: 130 alive / 82 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32753
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
