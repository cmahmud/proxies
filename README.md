# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 486
- HTTP: 145 alive / 102 gold
- HTTPS: 127 alive / 45 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44933
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
