# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 394
- HTTP: 323 alive / 88 gold
- HTTPS: 202 alive / 31 gold
- SOCKS4: 239 alive / 150 gold
- SOCKS5: 236 alive / 125 gold

## Historical pool

- Discovered: 160988
- Ever alive: 30874
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
