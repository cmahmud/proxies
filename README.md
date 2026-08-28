# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 444
- HTTP: 131 alive / 88 gold
- HTTPS: 134 alive / 22 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42224
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
