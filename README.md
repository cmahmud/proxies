# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 403
- HTTP: 262 alive / 94 gold
- HTTPS: 213 alive / 25 gold
- SOCKS4: 229 alive / 158 gold
- SOCKS5: 209 alive / 126 gold

## Historical pool

- Discovered: 160981
- Ever alive: 30852
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
