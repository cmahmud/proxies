# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 323
- HTTP: 247 alive / 38 gold
- HTTPS: 169 alive / 9 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 221 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 13998
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
