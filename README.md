# SyndProxy private pool

## Current pool

- Alive now: 1332
- Gold now: 576
- HTTP: 474 alive / 177 gold
- HTTPS: 337 alive / 93 gold
- SOCKS4: 243 alive / 141 gold
- SOCKS5: 278 alive / 165 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23180
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
