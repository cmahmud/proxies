# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 368
- HTTP: 287 alive / 73 gold
- HTTPS: 178 alive / 23 gold
- SOCKS4: 188 alive / 129 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
