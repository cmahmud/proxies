# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 400
- HTTP: 158 alive / 77 gold
- HTTPS: 134 alive / 20 gold
- SOCKS4: 197 alive / 155 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26757
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
