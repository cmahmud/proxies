# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 373
- HTTP: 71 alive / 39 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 172874
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
