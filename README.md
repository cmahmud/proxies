# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 400
- HTTP: 297 alive / 90 gold
- HTTPS: 239 alive / 33 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 232 alive / 129 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30996
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
