# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 409
- HTTP: 276 alive / 81 gold
- HTTPS: 188 alive / 20 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 240 alive / 163 gold

## Historical pool

- Discovered: 157410
- Ever alive: 29683
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
