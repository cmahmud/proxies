# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 410
- HTTP: 91 alive / 66 gold
- HTTPS: 99 alive / 20 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42650
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
