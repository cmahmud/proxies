# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 405
- HTTP: 383 alive / 105 gold
- HTTPS: 243 alive / 26 gold
- SOCKS4: 229 alive / 133 gold
- SOCKS5: 237 alive / 141 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30621
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
