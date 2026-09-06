# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 367
- HTTP: 71 alive / 52 gold
- HTTPS: 34 alive / 11 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48301
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
