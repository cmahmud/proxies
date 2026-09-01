# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 424
- HTTP: 93 alive / 67 gold
- HTTPS: 45 alive / 25 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
