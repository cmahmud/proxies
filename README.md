# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 522
- HTTP: 415 alive / 161 gold
- HTTPS: 257 alive / 85 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 215 alive / 135 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18511
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
