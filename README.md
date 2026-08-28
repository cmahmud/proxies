# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 425
- HTTP: 111 alive / 81 gold
- HTTPS: 148 alive / 17 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42295
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
