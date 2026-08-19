# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 354
- HTTP: 274 alive / 76 gold
- HTTPS: 228 alive / 9 gold
- SOCKS4: 210 alive / 124 gold
- SOCKS5: 228 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20286
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
