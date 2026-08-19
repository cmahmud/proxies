# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 343
- HTTP: 301 alive / 69 gold
- HTTPS: 184 alive / 17 gold
- SOCKS4: 193 alive / 112 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16172
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
