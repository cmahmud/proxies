# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 398
- HTTP: 185 alive / 75 gold
- HTTPS: 159 alive / 19 gold
- SOCKS4: 216 alive / 153 gold
- SOCKS5: 217 alive / 151 gold

## Historical pool

- Discovered: 149506
- Ever alive: 26777
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
