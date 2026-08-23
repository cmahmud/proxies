# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 390
- HTTP: 140 alive / 64 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 192 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33132
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
