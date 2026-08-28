# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 436
- HTTP: 123 alive / 85 gold
- HTTPS: 139 alive / 21 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42337
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
