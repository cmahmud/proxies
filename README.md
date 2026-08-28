# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 412
- HTTP: 95 alive / 67 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42629
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
