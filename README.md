# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 359
- HTTP: 330 alive / 71 gold
- HTTPS: 238 alive / 12 gold
- SOCKS4: 212 alive / 130 gold
- SOCKS5: 247 alive / 146 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20353
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
