# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 241
- HTTP: 440 alive / 31 gold
- HTTPS: 164 alive / 7 gold
- SOCKS4: 219 alive / 110 gold
- SOCKS5: 222 alive / 93 gold

## Historical pool

- Discovered: 91718
- Ever alive: 9071
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
