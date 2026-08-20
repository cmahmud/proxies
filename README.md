# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 394
- HTTP: 197 alive / 73 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 214 alive / 151 gold
- SOCKS5: 224 alive / 152 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26781
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
