# SyndProxy private pool

## Current pool

- Alive now: 597
- Gold now: 183
- HTTP: 173 alive / 32 gold
- HTTPS: 95 alive / 10 gold
- SOCKS4: 169 alive / 77 gold
- SOCKS5: 160 alive / 64 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
