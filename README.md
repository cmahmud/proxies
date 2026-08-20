# SyndProxy private pool

## Current pool

- Alive now: 679
- Gold now: 374
- HTTP: 181 alive / 72 gold
- HTTPS: 108 alive / 19 gold
- SOCKS4: 192 alive / 142 gold
- SOCKS5: 198 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25649
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
