# SyndProxy private pool

## Current pool

- Alive now: 1351
- Gold now: 543
- HTTP: 523 alive / 187 gold
- HTTPS: 353 alive / 53 gold
- SOCKS4: 234 alive / 146 gold
- SOCKS5: 241 alive / 157 gold

## Historical pool

- Discovered: 125596
- Ever alive: 19575
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
