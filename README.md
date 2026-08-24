# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 401
- HTTP: 104 alive / 63 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33657
- Ever gold: 1247

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
