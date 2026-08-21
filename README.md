# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 407
- HTTP: 263 alive / 88 gold
- HTTPS: 175 alive / 20 gold
- SOCKS4: 186 alive / 134 gold
- SOCKS5: 229 alive / 165 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29487
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
