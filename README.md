# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 400
- HTTP: 113 alive / 64 gold
- HTTPS: 180 alive / 16 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40582
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
