# SyndProxy private pool

## Current pool

- Alive now: 693
- Gold now: 356
- HTTP: 180 alive / 65 gold
- HTTPS: 145 alive / 16 gold
- SOCKS4: 185 alive / 133 gold
- SOCKS5: 183 alive / 142 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26669
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
