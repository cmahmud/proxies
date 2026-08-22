# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 401
- HTTP: 199 alive / 91 gold
- HTTPS: 145 alive / 31 gold
- SOCKS4: 186 alive / 127 gold
- SOCKS5: 236 alive / 152 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31921
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
