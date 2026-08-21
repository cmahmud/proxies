# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 444
- HTTP: 316 alive / 91 gold
- HTTPS: 206 alive / 26 gold
- SOCKS4: 222 alive / 161 gold
- SOCKS5: 231 alive / 166 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29493
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
