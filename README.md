# SyndProxy private pool

## Current pool

- Alive now: 1116
- Gold now: 522
- HTTP: 424 alive / 159 gold
- HTTPS: 247 alive / 81 gold
- SOCKS4: 206 alive / 133 gold
- SOCKS5: 239 alive / 149 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18763
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
