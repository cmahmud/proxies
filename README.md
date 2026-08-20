# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 366
- HTTP: 183 alive / 65 gold
- HTTPS: 140 alive / 17 gold
- SOCKS4: 199 alive / 134 gold
- SOCKS5: 203 alive / 150 gold

## Historical pool

- Discovered: 145549
- Ever alive: 25408
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
