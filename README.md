# SyndProxy private pool

## Current pool

- Alive now: 1211
- Gold now: 402
- HTTP: 420 alive / 92 gold
- HTTPS: 300 alive / 15 gold
- SOCKS4: 239 alive / 131 gold
- SOCKS5: 252 alive / 164 gold

## Historical pool

- Discovered: 131862
- Ever alive: 21362
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
