# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 431
- HTTP: 323 alive / 97 gold
- HTTPS: 235 alive / 36 gold
- SOCKS4: 186 alive / 126 gold
- SOCKS5: 281 alive / 172 gold

## Historical pool

- Discovered: 161919
- Ever alive: 31149
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
