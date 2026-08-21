# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 445
- HTTP: 326 alive / 106 gold
- HTTPS: 215 alive / 30 gold
- SOCKS4: 211 alive / 151 gold
- SOCKS5: 255 alive / 158 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28582
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
