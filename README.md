# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 367
- HTTP: 77 alive / 49 gold
- HTTPS: 41 alive / 9 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
