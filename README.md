# SyndProxy private pool

## Current pool

- Alive now: 667
- Gold now: 379
- HTTP: 179 alive / 60 gold
- HTTPS: 91 alive / 21 gold
- SOCKS4: 192 alive / 149 gold
- SOCKS5: 205 alive / 149 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25731
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
