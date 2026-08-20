# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 366
- HTTP: 195 alive / 84 gold
- HTTPS: 133 alive / 22 gold
- SOCKS4: 217 alive / 132 gold
- SOCKS5: 199 alive / 128 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26604
- Ever gold: 1083

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
