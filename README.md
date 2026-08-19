# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 515
- HTTP: 329 alive / 150 gold
- HTTPS: 254 alive / 90 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 202 alive / 126 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17611
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
