# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 427
- HTTP: 112 alive / 80 gold
- HTTPS: 125 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42425
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
