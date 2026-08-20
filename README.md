# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 352
- HTTP: 177 alive / 72 gold
- HTTPS: 173 alive / 19 gold
- SOCKS4: 202 alive / 134 gold
- SOCKS5: 208 alive / 127 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26718
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
