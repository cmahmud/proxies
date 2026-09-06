# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 406
- HTTP: 113 alive / 79 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 174 alive / 151 gold
- SOCKS5: 187 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48068
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
