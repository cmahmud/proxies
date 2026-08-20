# SyndProxy private pool

## Current pool

- Alive now: 1309
- Gold now: 581
- HTTP: 536 alive / 190 gold
- HTTPS: 335 alive / 98 gold
- SOCKS4: 213 alive / 138 gold
- SOCKS5: 225 alive / 155 gold

## Historical pool

- Discovered: 136253
- Ever alive: 22782
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
