# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 410
- HTTP: 231 alive / 90 gold
- HTTPS: 160 alive / 23 gold
- SOCKS4: 206 alive / 140 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29069
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
