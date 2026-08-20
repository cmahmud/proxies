# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 373
- HTTP: 150 alive / 63 gold
- HTTPS: 94 alive / 19 gold
- SOCKS4: 189 alive / 148 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25694
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
