# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 398
- HTTP: 111 alive / 67 gold
- HTTPS: 56 alive / 13 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33278
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
