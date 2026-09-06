# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 329
- HTTP: 83 alive / 62 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 151 alive / 134 gold
- SOCKS5: 157 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48381
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
