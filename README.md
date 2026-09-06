# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 407
- HTTP: 127 alive / 79 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 164 alive / 146 gold
- SOCKS5: 190 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48047
- Ever gold: 1515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
