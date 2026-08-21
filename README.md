# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 367
- HTTP: 307 alive / 96 gold
- HTTPS: 192 alive / 25 gold
- SOCKS4: 222 alive / 137 gold
- SOCKS5: 204 alive / 109 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28979
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
