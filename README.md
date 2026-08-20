# SyndProxy private pool

## Current pool

- Alive now: 1975
- Gold now: 658
- HTTP: 783 alive / 227 gold
- HTTPS: 623 alive / 119 gold
- SOCKS4: 247 alive / 146 gold
- SOCKS5: 322 alive / 166 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24342
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
