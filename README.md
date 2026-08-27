# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 407
- HTTP: 97 alive / 60 gold
- HTTPS: 101 alive / 18 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41475
- Ever gold: 1334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
