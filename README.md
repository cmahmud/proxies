# SyndProxy private pool

## Current pool

- Alive now: 1220
- Gold now: 411
- HTTP: 449 alive / 91 gold
- HTTPS: 260 alive / 17 gold
- SOCKS4: 239 alive / 142 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 131819
- Ever alive: 20934
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
