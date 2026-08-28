# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 429
- HTTP: 105 alive / 78 gold
- HTTPS: 119 alive / 23 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42455
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
