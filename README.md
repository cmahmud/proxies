# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 444
- HTTP: 119 alive / 87 gold
- HTTPS: 135 alive / 23 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42234
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
