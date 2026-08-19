# SyndProxy private pool

## Current pool

- Alive now: 1205
- Gold now: 540
- HTTP: 441 alive / 187 gold
- HTTPS: 333 alive / 78 gold
- SOCKS4: 221 alive / 132 gold
- SOCKS5: 210 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19804
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
