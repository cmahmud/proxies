# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 389
- HTTP: 250 alive / 80 gold
- HTTPS: 193 alive / 25 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 219 alive / 143 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27471
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
