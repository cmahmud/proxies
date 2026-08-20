# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 372
- HTTP: 170 alive / 71 gold
- HTTPS: 150 alive / 24 gold
- SOCKS4: 193 alive / 134 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26648
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
