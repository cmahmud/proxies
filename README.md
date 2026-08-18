# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 342
- HTTP: 259 alive / 49 gold
- HTTPS: 181 alive / 13 gold
- SOCKS4: 223 alive / 134 gold
- SOCKS5: 219 alive / 146 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14926
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
