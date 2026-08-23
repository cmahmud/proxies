# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 198
- HTTP: 205 alive / 44 gold
- HTTPS: 64 alive / 6 gold
- SOCKS4: 99 alive / 67 gold
- SOCKS5: 134 alive / 81 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32753
- Ever gold: 1208

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
