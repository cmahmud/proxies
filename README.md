# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 541
- HTTP: 347 alive / 153 gold
- HTTPS: 256 alive / 103 gold
- SOCKS4: 210 alive / 150 gold
- SOCKS5: 205 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19904
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
