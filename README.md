# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 377
- HTTP: 86 alive / 59 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 179 alive / 154 gold
- SOCKS5: 181 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48126
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
