# SyndProxy private pool

## Current pool

- Alive now: 1227
- Gold now: 539
- HTTP: 441 alive / 176 gold
- HTTPS: 344 alive / 58 gold
- SOCKS4: 230 alive / 155 gold
- SOCKS5: 212 alive / 150 gold

## Historical pool

- Discovered: 127332
- Ever alive: 19711
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
