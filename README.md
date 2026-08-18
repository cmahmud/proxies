# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 250
- HTTP: 272 alive / 29 gold
- HTTPS: 136 alive / 7 gold
- SOCKS4: 229 alive / 122 gold
- SOCKS5: 229 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9081
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
