# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 186
- HTTP: 246 alive / 32 gold
- HTTPS: 128 alive / 10 gold
- SOCKS4: 220 alive / 77 gold
- SOCKS5: 169 alive / 67 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
