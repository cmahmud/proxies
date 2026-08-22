# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 428
- HTTP: 248 alive / 80 gold
- HTTPS: 240 alive / 25 gold
- SOCKS4: 203 alive / 151 gold
- SOCKS5: 252 alive / 172 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31222
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
