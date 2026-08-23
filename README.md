# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 200
- HTTP: 228 alive / 36 gold
- HTTPS: 41 alive / 7 gold
- SOCKS4: 187 alive / 69 gold
- SOCKS5: 158 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32769
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
