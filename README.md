# SyndProxy private pool

## Current pool

- Alive now: 685
- Gold now: 385
- HTTP: 167 alive / 67 gold
- HTTPS: 107 alive / 17 gold
- SOCKS4: 206 alive / 147 gold
- SOCKS5: 205 alive / 154 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25691
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
