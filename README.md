# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 417
- HTTP: 286 alive / 91 gold
- HTTPS: 181 alive / 24 gold
- SOCKS4: 213 alive / 155 gold
- SOCKS5: 227 alive / 147 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30063
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
