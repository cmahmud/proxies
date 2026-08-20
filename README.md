# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 385
- HTTP: 238 alive / 80 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 252 alive / 141 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25286
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
