# SyndProxy private pool

## Current pool

- Alive now: 619
- Gold now: 379
- HTTP: 161 alive / 74 gold
- HTTPS: 87 alive / 19 gold
- SOCKS4: 189 alive / 143 gold
- SOCKS5: 182 alive / 143 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25646
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
