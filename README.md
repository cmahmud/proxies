# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 388
- HTTP: 133 alive / 62 gold
- HTTPS: 50 alive / 14 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 194 alive / 159 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
