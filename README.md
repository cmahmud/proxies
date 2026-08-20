# SyndProxy private pool

## Current pool

- Alive now: 1780
- Gold now: 649
- HTTP: 652 alive / 225 gold
- HTTPS: 582 alive / 120 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 313 alive / 157 gold

## Historical pool

- Discovered: 142697
- Ever alive: 24310
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
