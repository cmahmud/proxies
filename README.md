# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 327
- HTTP: 370 alive / 38 gold
- HTTPS: 202 alive / 10 gold
- SOCKS4: 238 alive / 147 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14127
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
