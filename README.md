# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 394
- HTTP: 340 alive / 76 gold
- HTTPS: 221 alive / 15 gold
- SOCKS4: 252 alive / 145 gold
- SOCKS5: 236 alive / 158 gold

## Historical pool

- Discovered: 131098
- Ever alive: 20522
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
