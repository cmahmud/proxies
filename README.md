# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 467
- HTTP: 122 alive / 94 gold
- HTTPS: 135 alive / 34 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 218 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46455
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
