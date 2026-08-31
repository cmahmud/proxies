# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 423
- HTTP: 92 alive / 67 gold
- HTTPS: 52 alive / 25 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45486
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
