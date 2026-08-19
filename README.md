# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 393
- HTTP: 330 alive / 99 gold
- HTTPS: 238 alive / 20 gold
- SOCKS4: 194 alive / 127 gold
- SOCKS5: 280 alive / 147 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22530
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
