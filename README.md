# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 391
- HTTP: 315 alive / 81 gold
- HTTPS: 232 alive / 23 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 244 alive / 144 gold

## Historical pool

- Discovered: 165502
- Ever alive: 32279
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
