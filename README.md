# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 439
- HTTP: 292 alive / 88 gold
- HTTPS: 192 alive / 22 gold
- SOCKS4: 212 alive / 161 gold
- SOCKS5: 231 alive / 168 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29492
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
