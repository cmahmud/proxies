# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 431
- HTTP: 110 alive / 79 gold
- HTTPS: 121 alive / 23 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42456
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
