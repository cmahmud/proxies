# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 399
- HTTP: 236 alive / 89 gold
- HTTPS: 166 alive / 18 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 230 alive / 141 gold

## Historical pool

- Discovered: 155698
- Ever alive: 29278
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
