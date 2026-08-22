# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 433
- HTTP: 338 alive / 99 gold
- HTTPS: 198 alive / 29 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 268 alive / 161 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32548
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
