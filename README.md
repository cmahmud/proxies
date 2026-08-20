# SyndProxy private pool

## Current pool

- Alive now: 1418
- Gold now: 562
- HTTP: 597 alive / 191 gold
- HTTPS: 381 alive / 96 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 212 alive / 132 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22800
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
