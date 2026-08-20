# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 577
- HTTP: 551 alive / 190 gold
- HTTPS: 343 alive / 98 gold
- SOCKS4: 215 alive / 138 gold
- SOCKS5: 217 alive / 151 gold

## Historical pool

- Discovered: 136253
- Ever alive: 22780
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
