# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 340
- HTTP: 76 alive / 60 gold
- HTTPS: 24 alive / 10 gold
- SOCKS4: 151 alive / 136 gold
- SOCKS5: 161 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
