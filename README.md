# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 395
- HTTP: 319 alive / 87 gold
- HTTPS: 252 alive / 24 gold
- SOCKS4: 239 alive / 135 gold
- SOCKS5: 238 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32086
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
