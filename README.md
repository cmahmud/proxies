# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 406
- HTTP: 93 alive / 64 gold
- HTTPS: 119 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42632
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
