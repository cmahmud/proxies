# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 418
- HTTP: 204 alive / 81 gold
- HTTPS: 153 alive / 26 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 251 alive / 170 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29336
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
