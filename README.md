# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 361
- HTTP: 69 alive / 54 gold
- HTTPS: 25 alive / 12 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 174 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48257
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
