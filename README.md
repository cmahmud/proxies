# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 559
- HTTP: 412 alive / 175 gold
- HTTPS: 326 alive / 84 gold
- SOCKS4: 237 alive / 151 gold
- SOCKS5: 224 alive / 149 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19761
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
