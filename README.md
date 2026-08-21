# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 387
- HTTP: 191 alive / 82 gold
- HTTPS: 110 alive / 22 gold
- SOCKS4: 210 alive / 135 gold
- SOCKS5: 209 alive / 148 gold

## Historical pool

- Discovered: 155681
- Ever alive: 29196
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
