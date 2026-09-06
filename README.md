# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 359
- HTTP: 77 alive / 47 gold
- HTTPS: 36 alive / 8 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48287
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
