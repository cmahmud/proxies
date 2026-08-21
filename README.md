# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 409
- HTTP: 364 alive / 106 gold
- HTTPS: 242 alive / 27 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 235 alive / 143 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30624
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
