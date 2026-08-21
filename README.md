# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 396
- HTTP: 234 alive / 76 gold
- HTTPS: 173 alive / 22 gold
- SOCKS4: 251 alive / 159 gold
- SOCKS5: 226 alive / 139 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29620
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
