# SyndProxy private pool

## Current pool

- Alive now: 1237
- Gold now: 462
- HTTP: 420 alive / 128 gold
- HTTPS: 326 alive / 73 gold
- SOCKS4: 235 alive / 117 gold
- SOCKS5: 256 alive / 144 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17265
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
