# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 420
- HTTP: 93 alive / 70 gold
- HTTPS: 109 alive / 20 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42493
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
