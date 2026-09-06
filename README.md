# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 321
- HTTP: 76 alive / 52 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 150 alive / 133 gold
- SOCKS5: 147 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48336
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
