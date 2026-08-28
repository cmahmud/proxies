# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 421
- HTTP: 101 alive / 74 gold
- HTTPS: 127 alive / 17 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42480
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
