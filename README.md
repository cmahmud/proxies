# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 390
- HTTP: 360 alive / 104 gold
- HTTPS: 248 alive / 22 gold
- SOCKS4: 204 alive / 121 gold
- SOCKS5: 295 alive / 143 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22630
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
