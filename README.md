# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 393
- HTTP: 308 alive / 82 gold
- HTTPS: 171 alive / 22 gold
- SOCKS4: 193 alive / 126 gold
- SOCKS5: 235 alive / 163 gold

## Historical pool

- Discovered: 151047
- Ever alive: 27128
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
