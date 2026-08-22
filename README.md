# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 422
- HTTP: 393 alive / 95 gold
- HTTPS: 240 alive / 35 gold
- SOCKS4: 196 alive / 131 gold
- SOCKS5: 240 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31128
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
