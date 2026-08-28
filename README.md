# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 412
- HTTP: 96 alive / 66 gold
- HTTPS: 102 alive / 20 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42664
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
