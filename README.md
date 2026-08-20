# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 394
- HTTP: 275 alive / 82 gold
- HTTPS: 217 alive / 27 gold
- SOCKS4: 199 alive / 131 gold
- SOCKS5: 248 alive / 154 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24959
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
