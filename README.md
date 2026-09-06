# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 390
- HTTP: 95 alive / 64 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48133
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
