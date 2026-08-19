# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 558
- HTTP: 365 alive / 161 gold
- HTTPS: 276 alive / 90 gold
- SOCKS4: 230 alive / 153 gold
- SOCKS5: 239 alive / 154 gold

## Historical pool

- Discovered: 122371
- Ever alive: 18554
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
