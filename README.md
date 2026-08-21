# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 431
- HTTP: 402 alive / 102 gold
- HTTPS: 278 alive / 27 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 278 alive / 159 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28119
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
