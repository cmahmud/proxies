# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 392
- HTTP: 409 alive / 100 gold
- HTTPS: 260 alive / 22 gold
- SOCKS4: 198 alive / 125 gold
- SOCKS5: 303 alive / 145 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22635
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
