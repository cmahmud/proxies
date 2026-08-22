# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 408
- HTTP: 206 alive / 90 gold
- HTTPS: 159 alive / 25 gold
- SOCKS4: 192 alive / 138 gold
- SOCKS5: 213 alive / 155 gold

## Historical pool

- Discovered: 162444
- Ever alive: 31447
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
