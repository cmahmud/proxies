# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 512
- HTTP: 364 alive / 148 gold
- HTTPS: 252 alive / 90 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 207 alive / 131 gold

## Historical pool

- Discovered: 117160
- Ever alive: 17672
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
