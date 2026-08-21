# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 432
- HTTP: 331 alive / 109 gold
- HTTPS: 205 alive / 32 gold
- SOCKS4: 247 alive / 149 gold
- SOCKS5: 250 alive / 142 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30762
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
