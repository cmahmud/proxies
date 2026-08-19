# SyndProxy private pool

## Current pool

- Alive now: 1398
- Gold now: 437
- HTTP: 487 alive / 93 gold
- HTTPS: 336 alive / 27 gold
- SOCKS4: 256 alive / 148 gold
- SOCKS5: 319 alive / 169 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22463
- Ever gold: 901

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
