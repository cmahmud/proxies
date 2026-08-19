# SyndProxy private pool

## Current pool

- Alive now: 1228
- Gold now: 399
- HTTP: 420 alive / 99 gold
- HTTPS: 283 alive / 22 gold
- SOCKS4: 211 alive / 132 gold
- SOCKS5: 314 alive / 146 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22520
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
