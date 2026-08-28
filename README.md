# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 429
- HTTP: 111 alive / 78 gold
- HTTPS: 122 alive / 22 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42461
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
