# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 425
- HTTP: 319 alive / 108 gold
- HTTPS: 225 alive / 26 gold
- SOCKS4: 232 alive / 153 gold
- SOCKS5: 239 alive / 138 gold

## Historical pool

- Discovered: 160022
- Ever alive: 30545
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
