# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 387
- HTTP: 95 alive / 60 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33124
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
