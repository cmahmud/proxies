# SyndProxy private pool

## Current pool

- Alive now: 723
- Gold now: 393
- HTTP: 171 alive / 80 gold
- HTTPS: 129 alive / 21 gold
- SOCKS4: 190 alive / 127 gold
- SOCKS5: 233 alive / 165 gold

## Historical pool

- Discovered: 151041
- Ever alive: 27117
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
