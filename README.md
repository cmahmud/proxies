# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 423
- HTTP: 127 alive / 72 gold
- HTTPS: 114 alive / 24 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35032
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
