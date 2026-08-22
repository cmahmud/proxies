# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 371
- HTTP: 428 alive / 79 gold
- HTTPS: 278 alive / 21 gold
- SOCKS4: 162 alive / 105 gold
- SOCKS5: 282 alive / 166 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32469
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
