# SyndProxy private pool

## Current pool

- Alive now: 609
- Gold now: 223
- HTTP: 193 alive / 33 gold
- HTTPS: 98 alive / 10 gold
- SOCKS4: 161 alive / 105 gold
- SOCKS5: 157 alive / 75 gold

## Historical pool

- Discovered: 86660
- Ever alive: 5728
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
