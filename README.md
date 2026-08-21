# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 442
- HTTP: 387 alive / 95 gold
- HTTPS: 244 alive / 35 gold
- SOCKS4: 223 alive / 155 gold
- SOCKS5: 259 alive / 157 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30250
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
