# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 420
- HTTP: 115 alive / 77 gold
- HTTPS: 129 alive / 21 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 198 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42388
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
