# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 344
- HTTP: 276 alive / 82 gold
- HTTPS: 176 alive / 30 gold
- SOCKS4: 199 alive / 137 gold
- SOCKS5: 190 alive / 95 gold

## Historical pool

- Discovered: 167110
- Ever alive: 32515
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
