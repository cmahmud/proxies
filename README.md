# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 413
- HTTP: 100 alive / 64 gold
- HTTPS: 174 alive / 20 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40712
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
