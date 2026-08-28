# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 410
- HTTP: 84 alive / 66 gold
- HTTPS: 91 alive / 18 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42641
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
