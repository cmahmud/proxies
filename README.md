# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 436
- HTTP: 283 alive / 98 gold
- HTTPS: 191 alive / 31 gold
- SOCKS4: 200 alive / 146 gold
- SOCKS5: 254 alive / 161 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32550
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
