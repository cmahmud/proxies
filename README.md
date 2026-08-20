# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 405
- HTTP: 214 alive / 76 gold
- HTTPS: 133 alive / 19 gold
- SOCKS4: 205 alive / 149 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25611
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
