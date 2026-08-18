# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 239
- HTTP: 415 alive / 31 gold
- HTTPS: 156 alive / 7 gold
- SOCKS4: 219 alive / 109 gold
- SOCKS5: 221 alive / 92 gold

## Historical pool

- Discovered: 91718
- Ever alive: 9064
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
