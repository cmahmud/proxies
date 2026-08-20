# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 371
- HTTP: 226 alive / 70 gold
- HTTPS: 138 alive / 17 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 194 alive / 135 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25487
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
