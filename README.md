# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 426
- HTTP: 309 alive / 93 gold
- HTTPS: 194 alive / 23 gold
- SOCKS4: 219 alive / 158 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30062
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
