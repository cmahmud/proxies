# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 411
- HTTP: 244 alive / 84 gold
- HTTPS: 171 alive / 26 gold
- SOCKS4: 187 alive / 132 gold
- SOCKS5: 251 alive / 169 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31486
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
