# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 524
- HTTP: 428 alive / 173 gold
- HTTPS: 328 alive / 57 gold
- SOCKS4: 219 alive / 149 gold
- SOCKS5: 206 alive / 145 gold

## Historical pool

- Discovered: 127332
- Ever alive: 19718
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
