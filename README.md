# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 405
- HTTP: 114 alive / 81 gold
- HTTPS: 71 alive / 18 gold
- SOCKS4: 169 alive / 151 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48083
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
