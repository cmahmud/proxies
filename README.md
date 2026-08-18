# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 243
- HTTP: 407 alive / 31 gold
- HTTPS: 139 alive / 6 gold
- SOCKS4: 231 alive / 141 gold
- SOCKS5: 154 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13646
- Ever gold: 427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
