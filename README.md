# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 365
- HTTP: 79 alive / 44 gold
- HTTPS: 54 alive / 10 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 186 alive / 157 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32996
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
