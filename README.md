# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 427
- HTTP: 99 alive / 77 gold
- HTTPS: 125 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42471
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
