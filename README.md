# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 376
- HTTP: 216 alive / 77 gold
- HTTPS: 239 alive / 21 gold
- SOCKS4: 195 alive / 137 gold
- SOCKS5: 204 alive / 141 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26507
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
