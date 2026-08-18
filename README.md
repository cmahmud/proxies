# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 352
- HTTP: 314 alive / 50 gold
- HTTPS: 204 alive / 14 gold
- SOCKS4: 238 alive / 147 gold
- SOCKS5: 229 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14840
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
