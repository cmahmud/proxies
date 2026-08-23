# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 386
- HTTP: 126 alive / 64 gold
- HTTPS: 68 alive / 11 gold
- SOCKS4: 182 alive / 153 gold
- SOCKS5: 195 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
