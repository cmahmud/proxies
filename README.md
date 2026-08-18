# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 345
- HTTP: 313 alive / 49 gold
- HTTPS: 226 alive / 14 gold
- SOCKS4: 238 alive / 144 gold
- SOCKS5: 225 alive / 138 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15099
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
