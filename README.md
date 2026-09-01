# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 459
- HTTP: 121 alive / 86 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 192 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46777
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
