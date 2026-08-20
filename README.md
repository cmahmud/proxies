# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 394
- HTTP: 212 alive / 69 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 230 alive / 164 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26032
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
