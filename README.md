# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 373
- HTTP: 70 alive / 39 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 172874
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
