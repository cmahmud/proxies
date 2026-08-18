# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 242
- HTTP: 336 alive / 29 gold
- HTTPS: 91 alive / 4 gold
- SOCKS4: 174 alive / 115 gold
- SOCKS5: 196 alive / 94 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10437
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
