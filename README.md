# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 261
- HTTP: 216 alive / 33 gold
- HTTPS: 106 alive / 8 gold
- SOCKS4: 231 alive / 127 gold
- SOCKS5: 227 alive / 93 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9088
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
