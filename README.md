# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 398
- HTTP: 446 alive / 100 gold
- HTTPS: 327 alive / 26 gold
- SOCKS4: 225 alive / 127 gold
- SOCKS5: 257 alive / 145 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28107
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
