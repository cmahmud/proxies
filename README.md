# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 391
- HTTP: 303 alive / 89 gold
- HTTPS: 229 alive / 21 gold
- SOCKS4: 195 alive / 123 gold
- SOCKS5: 262 alive / 158 gold

## Historical pool

- Discovered: 164917
- Ever alive: 32144
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
