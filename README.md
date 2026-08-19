# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 518
- HTTP: 326 alive / 150 gold
- HTTPS: 218 alive / 89 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 210 alive / 130 gold

## Historical pool

- Discovered: 117160
- Ever alive: 17653
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
