# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 372
- HTTP: 312 alive / 80 gold
- HTTPS: 227 alive / 23 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 242 alive / 127 gold

## Historical pool

- Discovered: 165819
- Ever alive: 32331
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
