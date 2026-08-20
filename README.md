# SyndProxy private pool

## Current pool

- Alive now: 1720
- Gold now: 636
- HTTP: 620 alive / 227 gold
- HTTPS: 555 alive / 101 gold
- SOCKS4: 234 alive / 147 gold
- SOCKS5: 311 alive / 161 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24323
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
