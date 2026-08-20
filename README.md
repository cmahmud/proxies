# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 366
- HTTP: 196 alive / 65 gold
- HTTPS: 114 alive / 19 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 205 alive / 140 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25424
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
