# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 293
- HTTP: 299 alive / 24 gold
- HTTPS: 192 alive / 4 gold
- SOCKS4: 253 alive / 146 gold
- SOCKS5: 245 alive / 119 gold

## Historical pool

- Discovered: 102806
- Ever alive: 12744
- Ever gold: 400

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
