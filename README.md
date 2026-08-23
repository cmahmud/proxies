# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 385
- HTTP: 118 alive / 65 gold
- HTTPS: 53 alive / 11 gold
- SOCKS4: 174 alive / 152 gold
- SOCKS5: 212 alive / 157 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
