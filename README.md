# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 385
- HTTP: 308 alive / 90 gold
- HTTPS: 240 alive / 34 gold
- SOCKS4: 193 alive / 134 gold
- SOCKS5: 231 alive / 127 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31278
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
