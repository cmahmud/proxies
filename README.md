# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 408
- HTTP: 375 alive / 95 gold
- HTTPS: 232 alive / 27 gold
- SOCKS4: 202 alive / 140 gold
- SOCKS5: 229 alive / 146 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31743
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
