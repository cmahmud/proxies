# SyndProxy private pool

## Current pool

- Alive now: 1120
- Gold now: 398
- HTTP: 413 alive / 97 gold
- HTTPS: 269 alive / 28 gold
- SOCKS4: 227 alive / 150 gold
- SOCKS5: 211 alive / 123 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30311
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
