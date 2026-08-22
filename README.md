# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 400
- HTTP: 266 alive / 95 gold
- HTTPS: 191 alive / 30 gold
- SOCKS4: 230 alive / 145 gold
- SOCKS5: 250 alive / 130 gold

## Historical pool

- Discovered: 161992
- Ever alive: 31311
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
