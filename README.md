# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 406
- HTTP: 105 alive / 66 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33657
- Ever gold: 1247

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
