# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 399
- HTTP: 290 alive / 86 gold
- HTTPS: 176 alive / 26 gold
- SOCKS4: 215 alive / 136 gold
- SOCKS5: 229 alive / 151 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32158
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
