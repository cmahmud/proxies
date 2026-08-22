# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 337
- HTTP: 318 alive / 82 gold
- HTTPS: 188 alive / 25 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 184 alive / 90 gold

## Historical pool

- Discovered: 167102
- Ever alive: 32508
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
