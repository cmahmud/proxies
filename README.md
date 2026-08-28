# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 412
- HTTP: 95 alive / 65 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42655
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
