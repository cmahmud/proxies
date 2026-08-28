# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 422
- HTTP: 92 alive / 72 gold
- HTTPS: 114 alive / 20 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42492
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
