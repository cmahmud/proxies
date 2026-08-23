# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 361
- HTTP: 113 alive / 37 gold
- HTTPS: 49 alive / 11 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32939
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
