# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 390
- HTTP: 111 alive / 56 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33361
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
