# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 412
- HTTP: 296 alive / 82 gold
- HTTPS: 218 alive / 26 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 262 alive / 169 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31194
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
