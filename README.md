# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 432
- HTTP: 315 alive / 85 gold
- HTTPS: 216 alive / 28 gold
- SOCKS4: 241 alive / 156 gold
- SOCKS5: 276 alive / 163 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32202
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
