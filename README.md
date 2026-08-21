# SyndProxy private pool

## Current pool

- Alive now: 1272
- Gold now: 398
- HTTP: 460 alive / 102 gold
- HTTPS: 327 alive / 27 gold
- SOCKS4: 226 alive / 125 gold
- SOCKS5: 259 alive / 144 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28099
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
