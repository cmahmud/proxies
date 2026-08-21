# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 413
- HTTP: 280 alive / 88 gold
- HTTPS: 191 alive / 21 gold
- SOCKS4: 216 alive / 144 gold
- SOCKS5: 241 alive / 160 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29433
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
