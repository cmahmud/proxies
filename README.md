# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 409
- HTTP: 212 alive / 83 gold
- HTTPS: 164 alive / 29 gold
- SOCKS4: 199 alive / 138 gold
- SOCKS5: 238 alive / 159 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31419
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
