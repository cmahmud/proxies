# SyndProxy private pool

## Current pool

- Alive now: 1468
- Gold now: 618
- HTTP: 556 alive / 218 gold
- HTTPS: 461 alive / 113 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 247 alive / 148 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23808
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
