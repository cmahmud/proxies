# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 582
- HTTP: 418 alive / 175 gold
- HTTPS: 321 alive / 148 gold
- SOCKS4: 198 alive / 125 gold
- SOCKS5: 185 alive / 134 gold

## Historical pool

- Discovered: 127416
- Ever alive: 19962
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
