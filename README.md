# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 367
- HTTP: 72 alive / 51 gold
- HTTPS: 31 alive / 10 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 179 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48302
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
