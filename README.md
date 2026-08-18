# SyndProxy private pool

## Current pool

- Alive now: 573
- Gold now: 228
- HTTP: 144 alive / 27 gold
- HTTPS: 75 alive / 7 gold
- SOCKS4: 155 alive / 111 gold
- SOCKS5: 199 alive / 83 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8361
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
