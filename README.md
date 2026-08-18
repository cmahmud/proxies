# SyndProxy private pool

## Current pool

- Alive now: 602
- Gold now: 183
- HTTP: 174 alive / 33 gold
- HTTPS: 96 alive / 10 gold
- SOCKS4: 172 alive / 76 gold
- SOCKS5: 160 alive / 64 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
