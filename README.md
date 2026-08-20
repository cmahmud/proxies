# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 368
- HTTP: 193 alive / 71 gold
- HTTPS: 141 alive / 19 gold
- SOCKS4: 194 alive / 118 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 148331
- Ever alive: 26063
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
