# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 431
- HTTP: 333 alive / 97 gold
- HTTPS: 262 alive / 34 gold
- SOCKS4: 181 alive / 131 gold
- SOCKS5: 257 alive / 169 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31169
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
