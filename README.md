# SyndProxy private pool

## Current pool

- Alive now: 1579
- Gold now: 626
- HTTP: 620 alive / 209 gold
- HTTPS: 492 alive / 114 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24030
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
