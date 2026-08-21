# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 386
- HTTP: 244 alive / 89 gold
- HTTPS: 197 alive / 18 gold
- SOCKS4: 185 alive / 137 gold
- SOCKS5: 217 alive / 142 gold

## Historical pool

- Discovered: 152163
- Ever alive: 27860
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
