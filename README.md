# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 382
- HTTP: 229 alive / 74 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 226 alive / 145 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25270
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
