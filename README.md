# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 427
- HTTP: 112 alive / 78 gold
- HTTPS: 117 alive / 20 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42461
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
