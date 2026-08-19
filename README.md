# SyndProxy private pool

## Current pool

- Alive now: 1123
- Gold now: 416
- HTTP: 371 alive / 86 gold
- HTTPS: 250 alive / 15 gold
- SOCKS4: 243 alive / 155 gold
- SOCKS5: 259 alive / 160 gold

## Historical pool

- Discovered: 131722
- Ever alive: 20773
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
