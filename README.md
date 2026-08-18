# SyndProxy private pool

## Current pool

- Alive now: 626
- Gold now: 216
- HTTP: 203 alive / 30 gold
- HTTPS: 73 alive / 8 gold
- SOCKS4: 149 alive / 96 gold
- SOCKS5: 201 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8727
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
