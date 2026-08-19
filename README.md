# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 540
- HTTP: 378 alive / 167 gold
- HTTPS: 258 alive / 92 gold
- SOCKS4: 205 alive / 138 gold
- SOCKS5: 215 alive / 143 gold

## Historical pool

- Discovered: 122387
- Ever alive: 18672
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
