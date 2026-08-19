# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 513
- HTTP: 347 alive / 160 gold
- HTTPS: 272 alive / 91 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 212 alive / 121 gold

## Historical pool

- Discovered: 119839
- Ever alive: 18368
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
