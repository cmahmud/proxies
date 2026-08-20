# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 395
- HTTP: 223 alive / 82 gold
- HTTPS: 100 alive / 20 gold
- SOCKS4: 209 alive / 142 gold
- SOCKS5: 212 alive / 151 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25978
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
