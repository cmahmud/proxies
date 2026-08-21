# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 456
- HTTP: 353 alive / 102 gold
- HTTPS: 234 alive / 34 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 279 alive / 171 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28705
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
