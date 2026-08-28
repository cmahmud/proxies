# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 428
- HTTP: 113 alive / 79 gold
- HTTPS: 114 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42430
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
