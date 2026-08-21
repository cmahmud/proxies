# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 412
- HTTP: 344 alive / 86 gold
- HTTPS: 223 alive / 26 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 272 alive / 155 gold

## Historical pool

- Discovered: 156427
- Ever alive: 29519
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
