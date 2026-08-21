# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 416
- HTTP: 330 alive / 88 gold
- HTTPS: 230 alive / 24 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 243 alive / 160 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29506
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
