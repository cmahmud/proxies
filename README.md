# SyndProxy private pool

## Current pool

- Alive now: 690
- Gold now: 353
- HTTP: 173 alive / 73 gold
- HTTPS: 140 alive / 21 gold
- SOCKS4: 188 alive / 130 gold
- SOCKS5: 189 alive / 129 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26635
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
