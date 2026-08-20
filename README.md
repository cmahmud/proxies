# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 393
- HTTP: 198 alive / 77 gold
- HTTPS: 155 alive / 17 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 225 alive / 148 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26789
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
