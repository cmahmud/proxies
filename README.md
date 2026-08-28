# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 422
- HTTP: 102 alive / 73 gold
- HTTPS: 115 alive / 20 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42485
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
