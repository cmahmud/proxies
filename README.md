# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 363
- HTTP: 105 alive / 37 gold
- HTTPS: 52 alive / 11 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 186 alive / 158 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32936
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
