# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 437
- HTTP: 116 alive / 87 gold
- HTTPS: 155 alive / 23 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42183
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
