# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 406
- HTTP: 207 alive / 87 gold
- HTTPS: 131 alive / 21 gold
- SOCKS4: 205 alive / 143 gold
- SOCKS5: 214 alive / 155 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25992
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
