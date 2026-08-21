# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 433
- HTTP: 349 alive / 110 gold
- HTTPS: 228 alive / 32 gold
- SOCKS4: 251 alive / 149 gold
- SOCKS5: 253 alive / 142 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30765
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
