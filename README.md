# SyndProxy private pool

## Current pool

- Alive now: 1308
- Gold now: 405
- HTTP: 458 alive / 96 gold
- HTTPS: 347 alive / 15 gold
- SOCKS4: 245 alive / 130 gold
- SOCKS5: 258 alive / 164 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21412
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
