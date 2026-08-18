# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 286
- HTTP: 375 alive / 28 gold
- HTTPS: 209 alive / 4 gold
- SOCKS4: 229 alive / 136 gold
- SOCKS5: 243 alive / 118 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12701
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
