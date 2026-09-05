# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 313
- HTTP: 113 alive / 79 gold
- HTTPS: 31 alive / 20 gold
- SOCKS4: 82 alive / 70 gold
- SOCKS5: 170 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47826
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
