# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 426
- HTTP: 102 alive / 65 gold
- HTTPS: 93 alive / 22 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 215 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35892
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
