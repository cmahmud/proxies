# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 406
- HTTP: 367 alive / 76 gold
- HTTPS: 227 alive / 21 gold
- SOCKS4: 218 alive / 155 gold
- SOCKS5: 231 alive / 154 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26801
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
