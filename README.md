# SyndProxy private pool

## Current pool

- Alive now: 640
- Gold now: 344
- HTTP: 163 alive / 70 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 176 alive / 122 gold
- SOCKS5: 194 alive / 134 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25576
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
