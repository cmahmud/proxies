# SyndProxy private pool

## Current pool

- Alive now: 1172
- Gold now: 246
- HTTP: 478 alive / 25 gold
- HTTPS: 254 alive / 10 gold
- SOCKS4: 208 alive / 109 gold
- SOCKS5: 232 alive / 102 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10159
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
