# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 431
- HTTP: 118 alive / 77 gold
- HTTPS: 92 alive / 24 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34664
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
