# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 345
- HTTP: 308 alive / 49 gold
- HTTPS: 191 alive / 15 gold
- SOCKS4: 250 alive / 143 gold
- SOCKS5: 225 alive / 138 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15102
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
