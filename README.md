# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 355
- HTTP: 184 alive / 63 gold
- HTTPS: 143 alive / 16 gold
- SOCKS4: 186 alive / 134 gold
- SOCKS5: 185 alive / 142 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26673
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
