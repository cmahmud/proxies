# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 374
- HTTP: 254 alive / 93 gold
- HTTPS: 175 alive / 19 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 215 alive / 117 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28944
- Ever gold: 1116

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
