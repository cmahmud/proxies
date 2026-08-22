# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 330
- HTTP: 313 alive / 80 gold
- HTTPS: 202 alive / 25 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 187 alive / 87 gold

## Historical pool

- Discovered: 167104
- Ever alive: 32510
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
