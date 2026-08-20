# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 373
- HTTP: 184 alive / 82 gold
- HTTPS: 110 alive / 22 gold
- SOCKS4: 198 alive / 136 gold
- SOCKS5: 221 alive / 133 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25950
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
