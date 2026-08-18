# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 210
- HTTP: 348 alive / 26 gold
- HTTPS: 141 alive / 9 gold
- SOCKS4: 206 alive / 96 gold
- SOCKS5: 205 alive / 79 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7913
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
