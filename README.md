# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 414
- HTTP: 350 alive / 90 gold
- HTTPS: 204 alive / 23 gold
- SOCKS4: 214 alive / 152 gold
- SOCKS5: 241 alive / 149 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30081
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
