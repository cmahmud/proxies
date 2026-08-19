# SyndProxy private pool

## Current pool

- Alive now: 1305
- Gold now: 400
- HTTP: 445 alive / 92 gold
- HTTPS: 284 alive / 17 gold
- SOCKS4: 248 alive / 146 gold
- SOCKS5: 328 alive / 145 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21675
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
