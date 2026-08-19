# SyndProxy private pool

## Current pool

- Alive now: 1187
- Gold now: 495
- HTTP: 418 alive / 145 gold
- HTTPS: 284 alive / 91 gold
- SOCKS4: 228 alive / 122 gold
- SOCKS5: 257 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17282
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
