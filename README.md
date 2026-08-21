# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 446
- HTTP: 351 alive / 106 gold
- HTTPS: 249 alive / 32 gold
- SOCKS4: 198 alive / 147 gold
- SOCKS5: 275 alive / 161 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28666
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
