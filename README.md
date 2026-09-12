# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 451
- HTTP: 124 alive / 96 gold
- HTTPS: 56 alive / 31 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49324
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
