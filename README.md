# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 361
- HTTP: 120 alive / 37 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 199 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32933
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
