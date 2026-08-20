# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 389
- HTTP: 197 alive / 81 gold
- HTTPS: 151 alive / 21 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 191 alive / 141 gold

## Historical pool

- Discovered: 149513
- Ever alive: 26921
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
