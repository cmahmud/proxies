# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 406
- HTTP: 390 alive / 80 gold
- HTTPS: 243 alive / 13 gold
- SOCKS4: 271 alive / 154 gold
- SOCKS5: 267 alive / 159 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20692
- Ever gold: 874

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
