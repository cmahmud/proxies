# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 431
- HTTP: 393 alive / 100 gold
- HTTPS: 290 alive / 24 gold
- SOCKS4: 278 alive / 150 gold
- SOCKS5: 255 alive / 157 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25158
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
