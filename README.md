# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 389
- HTTP: 255 alive / 79 gold
- HTTPS: 203 alive / 25 gold
- SOCKS4: 229 alive / 141 gold
- SOCKS5: 217 alive / 144 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27471
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
