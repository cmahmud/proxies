# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 414
- HTTP: 435 alive / 93 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 240 alive / 159 gold

## Historical pool

- Discovered: 162974
- Ever alive: 31680
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
