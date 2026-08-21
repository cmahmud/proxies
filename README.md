# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 367
- HTTP: 279 alive / 81 gold
- HTTPS: 226 alive / 23 gold
- SOCKS4: 182 alive / 115 gold
- SOCKS5: 242 alive / 148 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29862
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
