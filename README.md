# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 364
- HTTP: 211 alive / 75 gold
- HTTPS: 163 alive / 23 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 229 alive / 136 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29661
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
