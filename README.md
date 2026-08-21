# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 371
- HTTP: 299 alive / 93 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 213 alive / 113 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28990
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
