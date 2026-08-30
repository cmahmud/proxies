# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 445
- HTTP: 120 alive / 83 gold
- HTTPS: 58 alive / 28 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43692
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
