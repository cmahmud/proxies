# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 449
- HTTP: 102 alive / 76 gold
- HTTPS: 109 alive / 32 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47423
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
