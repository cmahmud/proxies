# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 527
- HTTP: 361 alive / 154 gold
- HTTPS: 247 alive / 89 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 210 alive / 135 gold

## Historical pool

- Discovered: 117176
- Ever alive: 17714
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
