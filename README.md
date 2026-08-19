# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 550
- HTTP: 425 alive / 169 gold
- HTTPS: 341 alive / 85 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 203 alive / 149 gold

## Historical pool

- Discovered: 127333
- Ever alive: 19756
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
