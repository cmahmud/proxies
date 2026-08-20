# SyndProxy private pool

## Current pool

- Alive now: 1470
- Gold now: 601
- HTTP: 574 alive / 209 gold
- HTTPS: 440 alive / 106 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 216 alive / 137 gold

## Historical pool

- Discovered: 140469
- Ever alive: 23741
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
