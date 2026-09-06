# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 363
- HTTP: 82 alive / 48 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 183 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48295
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
