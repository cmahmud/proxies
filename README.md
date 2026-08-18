# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 291
- HTTP: 260 alive / 47 gold
- HTTPS: 193 alive / 9 gold
- SOCKS4: 223 alive / 109 gold
- SOCKS5: 215 alive / 126 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14455
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
