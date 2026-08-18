# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 323
- HTTP: 362 alive / 36 gold
- HTTPS: 204 alive / 9 gold
- SOCKS4: 242 alive / 146 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14127
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
