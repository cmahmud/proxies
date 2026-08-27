# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 407
- HTTP: 96 alive / 60 gold
- HTTPS: 102 alive / 18 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41474
- Ever gold: 1334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
