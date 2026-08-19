# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 523
- HTTP: 353 alive / 162 gold
- HTTPS: 269 alive / 86 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 201 alive / 135 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18430
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
