# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 254
- HTTP: 228 alive / 29 gold
- HTTPS: 131 alive / 8 gold
- SOCKS4: 214 alive / 136 gold
- SOCKS5: 187 alive / 81 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9667
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
