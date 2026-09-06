# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 366
- HTTP: 72 alive / 51 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 177 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48301
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
