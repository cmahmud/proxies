# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 422
- HTTP: 322 alive / 97 gold
- HTTPS: 270 alive / 29 gold
- SOCKS4: 252 alive / 150 gold
- SOCKS5: 253 alive / 146 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25195
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
