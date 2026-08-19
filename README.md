# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 539
- HTTP: 422 alive / 186 gold
- HTTPS: 328 alive / 78 gold
- SOCKS4: 228 alive / 132 gold
- SOCKS5: 210 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19806
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
