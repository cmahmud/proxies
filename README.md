# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 406
- HTTP: 92 alive / 64 gold
- HTTPS: 115 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42633
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
