# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 361
- HTTP: 111 alive / 37 gold
- HTTPS: 57 alive / 10 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 188 alive / 155 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32926
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
