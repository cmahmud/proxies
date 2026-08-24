# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 399
- HTTP: 112 alive / 65 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33655
- Ever gold: 1246

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
