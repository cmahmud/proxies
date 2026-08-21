# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 367
- HTTP: 308 alive / 79 gold
- HTTPS: 203 alive / 19 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 240 alive / 145 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29857
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
