# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 380
- HTTP: 275 alive / 86 gold
- HTTPS: 206 alive / 26 gold
- SOCKS4: 193 alive / 126 gold
- SOCKS5: 210 alive / 142 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27284
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
