# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 361
- HTTP: 112 alive / 37 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32939
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
