# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 434
- HTTP: 363 alive / 110 gold
- HTTPS: 236 alive / 27 gold
- SOCKS4: 231 alive / 154 gold
- SOCKS5: 235 alive / 143 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30559
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
