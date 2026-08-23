# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 389
- HTTP: 126 alive / 66 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 208 alive / 157 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
