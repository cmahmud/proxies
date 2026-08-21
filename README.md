# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 419
- HTTP: 218 alive / 82 gold
- HTTPS: 134 alive / 26 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 259 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29337
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
