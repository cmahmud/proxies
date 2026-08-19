# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 406
- HTTP: 400 alive / 93 gold
- HTTPS: 251 alive / 17 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 289 alive / 154 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20874
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
