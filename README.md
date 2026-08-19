# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 476
- HTTP: 326 alive / 121 gold
- HTTPS: 225 alive / 90 gold
- SOCKS4: 188 alive / 128 gold
- SOCKS5: 227 alive / 137 gold

## Historical pool

- Discovered: 117144
- Ever alive: 17556
- Ever gold: 670

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
