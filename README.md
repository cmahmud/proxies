# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 367
- HTTP: 191 alive / 67 gold
- HTTPS: 146 alive / 20 gold
- SOCKS4: 194 alive / 118 gold
- SOCKS5: 230 alive / 162 gold

## Historical pool

- Discovered: 148332
- Ever alive: 26074
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
