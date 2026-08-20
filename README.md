# SyndProxy private pool

## Current pool

- Alive now: 1652
- Gold now: 622
- HTTP: 628 alive / 209 gold
- HTTPS: 468 alive / 117 gold
- SOCKS4: 220 alive / 136 gold
- SOCKS5: 336 alive / 160 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23927
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
