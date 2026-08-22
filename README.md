# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 399
- HTTP: 315 alive / 89 gold
- HTTPS: 255 alive / 29 gold
- SOCKS4: 193 alive / 141 gold
- SOCKS5: 225 alive / 140 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32082
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
