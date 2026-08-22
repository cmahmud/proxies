# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 437
- HTTP: 266 alive / 99 gold
- HTTPS: 193 alive / 29 gold
- SOCKS4: 221 alive / 145 gold
- SOCKS5: 269 alive / 164 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31042
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
